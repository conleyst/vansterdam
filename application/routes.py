from application import app
from application.forms import LoginForm
from flask import flash, redirect, render_template, url_for


@app.route("/")
@app.route("/index")
def index():
    user = {"name": "Sean"}
    adventures = [
        {"location": "Weesp", "description": "Eating cookies"},
        {"location": "Durgerdam", "description": "Biking against the wind"},
    ]

    return render_template(
        "index.html", pagetitle="Homepage", user=user, adventures=adventures
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data, form.remember_me.data)
        flash(
            f"Login requested for user: {form.username.data}, Remember Me: {form.remember_me.data}"
        )
        return redirect(url_for("index"))

    return render_template("login.html", pagetitle="Sign In", form=form)
