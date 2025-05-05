# ---------------------------------------------
# Auteur   : LM-Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------


from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models import Task, Project, User, Assignment
from app.forms import TaskForm

bp = Blueprint("tasks", __name__)

def _fill_task_form_choices(form: TaskForm):
    form.project_id.choices = [(p.id, p.name) for p in Project.query.order_by(Project.name)]
    form.assignees.choices  = [(u.id, u.username) for u in User.query.order_by(User.username)]

@bp.route("/")
@login_required
def list_tasks():
    tasks = Task.query.order_by(Task.created.desc()).all()
    return render_template("tasks/list.html", tasks=tasks)

@bp.route("/create", methods=["GET", "POST"])
@login_required
def create_task():
    form = TaskForm()
    _fill_task_form_choices(form)
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            project_id=form.project_id.data,
            status=form.status.data,
            priority=form.priority.data,
            due_date=form.due_date.data,
            description=form.description.data
        )
        db.session.add(task)
        db.session.flush()   # pour avoir task.id avant assignments

        for uid in form.assignees.data:
            db.session.add(Assignment(user_id=uid, task=task))

        db.session.commit()
        flash("Tâche créée 🚀", "success")
        return redirect(url_for("tasks.list_tasks"))
    return render_template("tasks/form.html", form=form, task=None)

@bp.route("/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)
    _fill_task_form_choices(form)

    if form.validate_on_submit():
        form.populate_obj(task)
        # mettre à jour assignees
        Assignment.query.filter_by(task_id=task.id).delete()
        for uid in form.assignees.data:
            db.session.add(Assignment(user_id=uid, task=task))
        db.session.commit()
        flash("Tâche mise à jour 👍", "success")
        return redirect(url_for("tasks.list_tasks"))

    # pré‑sélection des assignees
    form.assignees.data = [a.user_id for a in task.assignees]
    return render_template("tasks/form.html", form=form, task=task)

@bp.route("/<int:task_id>/delete")
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Tâche supprimée 🗑️", "info")
    return redirect(url_for("tasks.list_tasks"))
