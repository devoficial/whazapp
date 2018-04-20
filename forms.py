from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp,
                                ValidationError, Email,
                                Length, EqualTo)

from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError("User already exists")


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError("Email already exists")


class RegisterForm(Form):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letter, "
                         "numbers, and underscores only"
                         )),
            name_exists
        ])

    email = StringField(
        "email",
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(min=4),
            EqualTo("password2", message="password must match")
        ])
    password2 = PasswordField(
        "Confirm password",
        validators=[DataRequired()])


class LoginForm(Form):
    email = StringField(
        "email",
        validators=[DataRequired(), Email()])
    password = PasswordField(
        "password",
        validators=[DataRequired()])

class PostForm(Form):
    content = TextAreaField("What's up ?", validators=[DataRequired()])
