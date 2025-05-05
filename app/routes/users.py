# ---------------------------------------------
# Auteur   : LM-Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------


from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import User
from app.forms import UserForm
from app.utils.decorators import role_required

bp = Blueprint("users", __name__)

@bp.route("/")
@login_required
def list_users():
    users = User.query.order_by(User.username).all()
    return render_template("users/list.html", users=users)

@bp.route("/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data.lower(),
            role=form.role.data
        )
        if form.password.data:
            user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Utilisateur créé ✔", "success")
        return redirect(url_for("users.list_users"))
    return render_template("users/form.html", form=form, user=None)

@bp.route("/<int:user_id>/edit", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if not current_user.is_admin() and current_user.id != user.id:
        flash("Accès refusé", "danger")
        return redirect(url_for("users.list_users"))

    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email    = form.email.data.lower()
        user.role     = form.role.data
        if form.password.data:
            user.set_password(form.password.data)
        db.session.commit()
        flash("Utilisateur mis à jour", "success")
        return redirect(url_for("users.list_users"))
    return render_template("users/form.html", form=form, user=user)

@bp.route("/<int:user_id>/delete")
@login_required
@role_required("admin")
def delete_user(user_id):
    if current_user.id == user_id:
        flash("Tu ne peux pas te supprimer toi‑même !", "warning")
        return redirect(url_for("users.list_users"))

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("Utilisateur supprimé 🗑️", "info")
    return redirect(url_for("users.list_users"))
