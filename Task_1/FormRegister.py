from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login_email = StringField("Login/Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    repeat_password = PasswordField("Repeat Password", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    specialty = StringField("Specialty", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")
