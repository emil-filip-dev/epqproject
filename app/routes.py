import os
from flask import send_from_directory, render_template, redirect
from werkzeug.exceptions import NotFound

from app import app


@app.route("/")
def index():
    return redirect("/index")


@app.route("/<string:page>")
def page(page):
    return render_template("main.html",
                           content="/html/" + page + ".html",
                           backVisibility="hidden",
                           nextVisibility="hidden")


@app.route("/html/<path:file>")
def html(file):
    return send_from_directory("html", file)


@app.route("/js/<path:file>")
def js(file):
    return send_from_directory("js", file)


@app.route("/css/<path:file>")
def css(file):
    return send_from_directory("css", file)


@app.route("/resources/<path:file>")
def rsrc(file):
    return send_from_directory("resources", file)


@app.route("/<string:tab>/<int:page>")
def tabbed_page(tab, page):
    back_page = page - 1
    next_page = page + 1
    back_visible = True
    next_visible = True
    if back_page == 0:
        back_visible = False
    try:
        send_from_directory("html", tab + "/" + str(next_page) + ".html")
    except NotFound:
        next_visible = False
    return render_template("main.html",
                           content="/html/" + tab + "/" + str(page) + ".html",
                           backLocation="/" + tab + "/" + str(back_page),
                           nextLocation="/" + tab + "/" + str(next_page),
                           backVisibility="visible" if back_visible else "hidden",
                           nextVisibility="visible" if next_visible else "hidden")


@app.route("/quiz")
def quiz():
    return render_template("main.html", content="/html/quiz.html")
