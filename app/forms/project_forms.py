from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class ProjectForm(FlaskForm):
    name        = StringField("Nom", validators=[DataRequired(), Length(max=128)])
    description = TextAreaField("Description")
    start_date  = DateField("Date début", format="%Y-%m-%d")
    end_date    = DateField("Date fin",   format="%Y-%m-%d")
    submit      = SubmitField("Enregistrer")
