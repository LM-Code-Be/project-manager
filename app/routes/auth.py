"""
Routes login / logout / register.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app import db
from app.forms import LoginForm, RegisterForm
from app.models import User

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Connexion réussie ✔", "success")
            next_page = request.args.get("next") or url_for("dashboard.index")
            return redirect(next_page)
        flash("Identifiants invalides 😕", "danger")
    return render_template("login.html", form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("À la prochaine !", "info")
    return redirect(url_for("auth.login"))

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data.lower()).first():
            flash("E‑mail déjà utilisé !", "warning")
        else:
            user = User(
                username=f"{form.first_name.data}.{form.last_name.data}".lower(),
                email=form.email.data.lower(),
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Compte créé, tu peux te connecter 👌", "success")
            return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)
