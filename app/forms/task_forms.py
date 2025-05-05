# ---------------------------------------------
# Auteur   : LM‑Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------
from flask_wtf import FlaskForm
from wtforms import (
    StringField, TextAreaField, SelectField, SelectMultipleField,
    DateField, SubmitField
)
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title       = StringField("Titre", validators=[DataRequired(), Length(max=140)])
    project_id  = SelectField("Projet", coerce=int, validators=[DataRequired()])
    status      = SelectField(
        "Statut",
        choices=[("todo", "À faire"), ("in_progress", "En cours"), ("done", "Terminé")],
        validators=[DataRequired()],
    )
    priority    = SelectField(
        "Priorité",
        choices=[("low", "Faible"), ("medium", "Moyenne"), ("high", "Élevée")],
        validators=[DataRequired()],
    )
    due_date    = DateField("Échéance", validators=[DataRequired()])
    assignees   = SelectMultipleField("Utilisateurs assignés", coerce=int)
    description = TextAreaField("Description")
    submit      = SubmitField("Enregistrer")
