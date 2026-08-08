from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(
                min=3,max=30,
                message="Username must be betwwen 3 and 30 characters."
            ),
            Regexp(
                r"^[A-Za-z0-9]+$",
                message="Username can contain only letters, numbers, and underscore."
            )
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Please entre a valid emal address."),
            Length(max=120)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(
                min=8,
                max=128,
                message="Password must contain at least 8 characters."
            )
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="Please confirm your password."),
            EqualTo(
                "password",
                message="Passwords must match."
            )
        ]
    )

    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(message="Email is required."),
        Email(message="Please enter a valid email address.")
        ]
    )

    password = PasswordField(
        "Password", validators=[
            DataRequired(message="Password is required.")
        ]
    )

    submit = SubmitField("Login")