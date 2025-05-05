# ---------------------------------------------
# Auteur   : LM‑Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------
from datetime import date
import calendar
from flask import Blueprint, render_template
from flask_login import login_required
from app import db
from app.models import Project, Task, User, Assignment  # Assignment = table d'association

bp = Blueprint("dashboard", __name__, url_prefix="/")

@bp.route("/")
@login_required
def index():
    # ---------- KPI ----------
    total_projects = Project.query.count()
    total_tasks    = Task.query.count()
    total_users    = User.query.count()
    overdue_tasks  = Task.query.filter(Task.due_date < date.today(),
                                       Task.status != "done").count()
    tasks_progress = Task.query.filter_by(status="in_progress").count()
    tasks_done     = Task.query.filter_by(status="done").count()

    # ---------- Graphique 1 : par statut ----------
    status_map = {"todo": "À faire", "in_progress": "En cours", "done": "Terminé"}
    status_data = (
        Task.query.with_entities(Task.status, db.func.count())
        .group_by(Task.status).all()
    )
    chart_status = {
        "labels": [status_map.get(s, s) for s, _ in status_data],
        "data":   [c for _, c in status_data],
    }

    # ---------- Graphique 2 : par utilisateur ----------
    user_data = (
        db.session.query(User.username, db.func.count(Task.id))
        .join(Assignment, Assignment.user_id == User.id)
        .join(Task, Task.id == Assignment.task_id)
        .group_by(User.username)
        .all()
    )
    chart_user = {
        "labels": [u for u, _ in user_data],
        "data":   [c for _, c in user_data],
    }

    # ---------- Graphique 3 : tâches créées par mois ----------
    monthly_data = (
        db.session.query(db.func.month(Task.created), db.func.count())
        .group_by(db.func.month(Task.created)).all()
    )
    monthly_labels = [calendar.month_abbr[m] for m in range(1, 13)]
    monthly_counts = {m: 0 for m in range(1, 13)}
    for m, count in monthly_data:
        monthly_counts[m] = count
    chart_monthly = {
        "labels": monthly_labels,
        "data":   [monthly_counts[m] for m in range(1, 13)],
    }

    # ---------- 5 prochaines tâches proches de l'échéance ----------
    upcoming_tasks = (
        Task.query.filter(Task.status != "done", Task.due_date >= date.today())
        .order_by(Task.due_date)
        .limit(5)
        .all()
    )

    return render_template(
        "dashboard.html",
        stats={
            "projects":  total_projects,
            "tasks":     total_tasks,
            "users":     total_users,
            "overdue":   overdue_tasks,
            "progress":  tasks_progress,
            "done":      tasks_done,
        },
        chart_monthly = chart_monthly,
        chart_status  = chart_status,
        chart_user    = chart_user,
        upcoming      = upcoming_tasks,
    )
