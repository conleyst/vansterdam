import os

from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user
from typing import Union
from vansterdam import app
from vansterdam.extensions import db
from vansterdam.forms import LoginForm, SignUpForm
from vansterdam.models import User
from werkzeug.wrappers.response import Response


SIGNUP_TOKEN = os.environ.get("SIGNUP_TOKEN")
ADMIN_SIGNUP_TOKEN = os.environ.get("ADMIN_SIGNUP_TOKEN")


@app.route("/")
@app.route("/index")
def index() -> str:
    """Define root."""

    user = {"name": "Sean"}
    adventures = [
        {"location": "Weesp", "description": "Eating cookies"},
        {"location": "Durgerdam", "description": "Biking against the wind"},
    ]

    return render_template(
        "index.html", pagetitle="Homepage", user=user, adventures=adventures
    )


@app.route("/login", methods=["GET", "POST"])
def login() -> Union[Response, str]:
    """
    Define login route.

    GET served content of login page.
    POST validates request and logs the user in.
    """

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user._check_password(form.password.data):
            flash("Invalid username or password.")
            return redirect(url_for("login"))
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("index"))

    return render_template("login.html", pagetitle="Sign In", form=form)


@app.route("signup", methods=["GET", "POST"])
def signup() -> Union[Response, str]:
    """
    Defines the sign-up route.

    GET serves content of sign-up page.
    POST validates request, creates the User object, and logs in as the created User.
    """

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = SignUpForm()
    if form.validate_on_submit():
        if form.signup_token.data not in (SIGNUP_TOKEN, ADMIN_SIGNUP_TOKEN):
            flash(
                "The sign-up token you entered is incorrect. Check that you entered correctly or contact the site creator."
            )
            return redirect(url_for("signup"))

        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user is not None:
            flash(
                "A user already exists with that username. Please choose a different one."
            )
            return redirect(url_for("signup"))

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            update_on_new_post=form.update_me.data,
            is_admin=(form.signup_token.data == ADMIN_SIGNUP_TOKEN),
        )

        new_user._set_password(form.username.password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("index"))

    return render_template("signup.html", pagetitle="Create An Account")
