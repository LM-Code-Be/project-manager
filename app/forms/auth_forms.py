"""
Forms de login & register (Flask-WTF).
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email    = StringField("E‑mail", validators=[DataRequired(), Email()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
    remember = BooleanField("Se souvenir")
    submit   = SubmitField("Connexion")

class RegisterForm(FlaskForm):
    first_name = StringField("Prénom", validators=[DataRequired(), Length(max=50)])
    last_name  = StringField("Nom",    validators=[DataRequired(), Length(max=50)])
    email      = StringField("E‑mail", validators=[DataRequired(), Email()])
    password   = PasswordField("Mot de passe", validators=[DataRequired(), Length(min=6)])
    confirm    = PasswordField("Confirmer", validators=[DataRequired(), EqualTo("password")])
    submit     = SubmitField("S’inscrire")
