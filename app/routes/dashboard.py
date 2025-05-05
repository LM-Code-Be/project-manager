from flask import Blueprint, render_template
from flask_login import login_required
from datetime import date
from app.models import Project, Task, User
from app import db
import calendar

bp = Blueprint("dashboard", __name__, url_prefix="/")

@bp.route("/")
@login_required
def index():
    # Statistiques globales
    total_projects = Project.query.count()
    total_tasks = Task.query.count()
    total_users = User.query.count()
    overdue_tasks = Task.query.filter(Task.due_date < date.today(), Task.status != "done").count()

    # Répartition des tâches par statut
    status_data = (
        Task.query.with_entities(Task.status, db.func.count())
        .group_by(Task.status).all()
    )
    status_map = {
        "todo": "À faire",
        "in_progress": "En cours",
        "done": "Terminé"
    }
    status_labels = [status_map.get(s, s) for s, _ in status_data]
    status_counts = [c for _, c in status_data]

    # Évolution mensuelle des tâches créées
    monthly_data = (
        db.session.query(db.func.month(Task.created), db.func.count())
        .group_by(db.func.month(Task.created)).all()
    )
    monthly_labels = [calendar.month_abbr[m] for m in range(1, 13)]
    monthly_counts = {m: 0 for m in range(1, 13)}
    for m, count in monthly_data:
        monthly_counts[m] = count
    tasks_by_month = [monthly_counts[m] for m in range(1, 13)]

    return render_template("dashboard.html",
        stats={
            "projects": total_projects,
            "tasks": total_tasks,
            "users": total_users,
            "overdue": overdue_tasks
        },
        chart_monthly={
            "labels": monthly_labels,
            "data": tasks_by_month
        },
        chart_status={
            "labels": status_labels,
            "data": status_counts
        }
    )
