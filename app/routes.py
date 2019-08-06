from flask import send_from_directory
from app import app


@app.route('/')
def index():
    return send_from_directory('html', filename="index.html")


@app.route('/<string:page>')
def html(page):
    return send_from_directory("html", filename=(page + ".html"))


@app.route('/<string:tab>/<string:page>')
def html_tab(tab, page):
    return send_from_directory(directory=("html/" + tab), filename=(page + ".html"))


@app.route('/js/<path:file>')
def js(file):
    return send_from_directory("js", filename=(file + ".js"))


@app.route('/css/<path:file>')
def css(file):
    return send_from_directory("css", filename=(file + ".css"))
