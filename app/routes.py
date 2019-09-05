from flask import send_from_directory, render_template, redirect, request
from werkzeug.exceptions import NotFound

from app import app


def using_browser(browser):
    user_browser = request.user_agent.browser
    return user_browser == browser


@app.route("/")
def index():
    return redirect("/index")


@app.route("/<string:page>")
def page(page):

    style = "main"
    # if using_browser("webkit") or using_browser("edge"):
    #     style = "main-ie"

    return render_template("main.html",
                           style="/css/" + style + ".css",
                           content="/html/" + page + ".html",
                           backVisibility="hidden",
                           nextVisibility="hidden")


@app.route("/<string:tab>/<int:page>")
def tabbed_page(tab, page):

    style = "main"
    # if using_browser("webkit") or using_browser("edge"):
    #     style = "main-ie"

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
                           style="/css/" + style + ".css",
                           content="/html/" + tab + "/" + str(page) + ".html",
                           backLocation="/" + tab + "/" + str(back_page),
                           nextLocation="/" + tab + "/" + str(next_page),
                           backVisibility="visible" if back_visible else "hidden",
                           nextVisibility="visible" if next_visible else "hidden")


@app.route("/quiz")
def quiz():
    return render_template("main.html", content="/html/quiz.html")


@app.route("/html/<path:file>")
def html(file):

    style = "content"
    # if using_browser("webkit") or using_browser("edge"):
    #     style = "content-ie"

    return render_template(file,
                           style="/css/" + style + ".css")


@app.route("/js/<path:file>")
def js(file):
    return send_from_directory("js", file)


@app.route("/css/<path:file>")
def css(file):
    return send_from_directory("css", file)


@app.route("/resources/<path:file>")
def rsrc(file):
    return send_from_directory("resources", file)
