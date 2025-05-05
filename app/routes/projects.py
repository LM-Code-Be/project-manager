# ---------------------------------------------
# Auteur   : LM-Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------


from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Project
from app.forms import ProjectForm
from app.utils.decorators import role_required

bp = Blueprint("projects", __name__)

@bp.route("/")
@login_required
def list_projects():
    projects = Project.query.order_by(Project.created.desc()).all()
    return render_template("projects/list.html", projects=projects)

@bp.route("/create", methods=["GET", "POST"])
@login_required
def create_project():
    form = ProjectForm()
    if form.validate_on_submit():
        proj = Project(
            name=form.name.data,
            description=form.description.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            owner=current_user
        )
        db.session.add(proj)
        db.session.commit()
        flash("Projet créé 🎉", "success")
        return redirect(url_for("projects.list_projects"))
    return render_template("projects/form.html", form=form, project=None)

@bp.route("/<int:project_id>/edit", methods=["GET", "POST"])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        form.populate_obj(project)
        db.session.commit()
        flash("Projet mis à jour ✅", "success")
        return redirect(url_for("projects.list_projects"))
    return render_template("projects/form.html", form=form, project=project)

@bp.route("/<int:project_id>/delete")
@login_required
@role_required("admin")
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash("Projet supprimé 🗑️", "info")
    return redirect(url_for("projects.list_projects"))
