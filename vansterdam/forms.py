from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "User Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password need to be at least 8 characters."),
        ],
    )
    password_confirmation = PasswordField(
        "Confirm User Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    signup_token = PasswordField(
        "Enter the sign-up token given to you by the site creator.",
        validators=[DataRequired()],
    )
    update_me = BooleanField("Send me an email when there's a new post.")
    submit = SubmitField("Sign Up")
