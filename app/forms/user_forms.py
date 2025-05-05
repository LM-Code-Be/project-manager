from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class UserForm(FlaskForm):
    username = StringField("Nom d’utilisateur", validators=[DataRequired(), Length(max=64)])
    email    = StringField("E‑mail", validators=[DataRequired(), Email(), Length(max=120)])
    role     = SelectField("Rôle", choices=[("member", "Membre"), ("admin", "Admin")])
    # password uniquement si création
    password = PasswordField("Mot de passe")
    confirm  = PasswordField("Confirmer", validators=[EqualTo("password", "Les mots de passe ne correspondent pas.")])
    submit   = SubmitField("Enregistrer")
