from application import app
from application.forms import LoginForm
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"name": "Sean"}
    adventures = [
        {"location": "Weesp", "description": "Eating cookies"},
        {"location": "Durgerdam", "description": "Biking against the wind"}
    ]

    return render_template("index.html", pagetitle="Homepage", user=user, adventures=adventures)


@app.route('/login')
def login():
    form = LoginForm()
    
    return render_template('login.html', title='Sign In', form=form)
