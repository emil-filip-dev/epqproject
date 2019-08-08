from flask import send_from_directory, render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("main.html", content="/html/index.html")


@app.route("/html/<path:file>")
def html(file):
    return send_from_directory("html", file)


@app.route("/js/<path:file>")
def js(file):
    return send_from_directory("js", file)


@app.route("/css/<path:file>")
def css(file):
    return send_from_directory("css", file)


@app.route("/<string:tab>/<string:page>")
def page(tab, page):
    return render_template("main.html", content=("/html/" + tab + "/" + page + ".html"))


@app.route("/quiz")
def quiz():
    return render_template("main.html", content="/html/quiz.html")
