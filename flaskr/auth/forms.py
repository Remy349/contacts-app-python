from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class SignInForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(message="Enter a username")])
    password = PasswordField("Password",
                             validators=[DataRequired(message="Enter a password")])
    submit = SubmitField("Sign In")
