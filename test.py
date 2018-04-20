from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(Form):
    email = StringField(
        #"email",
        Validators=[
            DataRequired(),
            Email()
        ])
    password = PasswordField()
