from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class WorksForm(FlaskForm):
    team_leader = IntegerField("Team Leader id", validators=[DataRequired()])
    job = StringField("Job Title", validators=[DataRequired()])
    work_size = StringField("Work Size", validators=[DataRequired()])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField("Submit")
