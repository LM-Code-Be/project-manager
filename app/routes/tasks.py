# ---------------------------------------------
# Auteur   : LM‑Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models import Task, User, Project, Assignment
from app.forms.task_forms import TaskForm

bp = Blueprint("tasks", __name__)

# -------- utilitaire pour les choix --------
def _fill_choices(form: TaskForm):
    form.project_id.choices = [(p.id, p.name) for p in Project.query.order_by(Project.name)]
    form.assignees.choices  = [(u.id, u.username) for u in User.query.order_by(User.username)]

# -------- liste --------
@bp.route("/")
@login_required
def list_tasks():
    tasks = Task.query.order_by(Task.due_date).all()
    return render_template("tasks/list.html", tasks=tasks)

# -------- création --------
@bp.route("/create", methods=["GET", "POST"])
@login_required
def create_task():
    form = TaskForm()
    _fill_choices(form)

    if form.validate_on_submit():
        task = Task(
            title       = form.title.data,
            description = form.description.data,
            status      = form.status.data,
            priority    = form.priority.data,
            due_date    = form.due_date.data,
            project_id  = form.project_id.data,
        )
        db.session.add(task)
        db.session.flush()          # pour obtenir task.id

        # créer les Assignment
        for uid in form.assignees.data:
            db.session.add(Assignment(user_id=uid, task_id=task.id))

        db.session.commit()
        flash("Tâche créée avec succès.", "success")
        return redirect(url_for("tasks.list_tasks"))

    return render_template("tasks/form.html", form=form, edit=False)

# -------- édition --------
@bp.route("/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)
    _fill_choices(form)

    # pré‑cocher les assignés existants
    if not form.assignees.data:
        form.assignees.data = [a.user_id for a in task.assignees]

    if form.validate_on_submit():
        # MAJ champs simples
        task.title       = form.title.data
        task.description = form.description.data
        task.status      = form.status.data
        task.priority    = form.priority.data
        task.due_date    = form.due_date.data
        task.project_id  = form.project_id.data

        # --- MAJ des assignés ---
        Assignment.query.filter_by(task_id=task.id).delete()      # retire tous
        for uid in form.assignees.data:                           # recrée
            db.session.add(Assignment(user_id=uid, task_id=task.id))

        db.session.commit()
        flash("Tâche mise à jour avec succès.", "success")
        return redirect(url_for("tasks.list_tasks"))

    return render_template("tasks/form.html", form=form, task=task, edit=True)

# -------- suppression --------
@bp.route("/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Tâche supprimée.", "info")
    return redirect(url_for("tasks.list_tasks"))
