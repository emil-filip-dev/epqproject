from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/page')
def page():
    return render_template("page.html")
