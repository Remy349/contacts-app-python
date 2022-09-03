from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from flaskr.models import User


class SignInForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(message="Enter a username")])
    password = PasswordField("Password",
                             validators=[DataRequired(message="Enter a password")])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class SignUpForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(message="Enter a username"),
                                       Length(min=5, max=30)])
    email = StringField("Email",
                        validators=[DataRequired(message="Enter a email adress"),
                                    Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(message="Enter a password"),
                                         Length(min=8, max=16)])
    password_again = PasswordField("Repeat Password",
                                   validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user is not None:
            raise ValidationError("Please use a different username!")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user is not None:
            raise ValidationError("Please use a different email adress!")
