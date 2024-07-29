from flask import render_template
from __main__ import app


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
