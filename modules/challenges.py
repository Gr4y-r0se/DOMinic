from flask import (
    render_template,
    request,
    redirect,
    make_response,
)
from urllib.parse import unquote_plus, urlparse
from __main__ import app


# Easy
@app.route("/challenge1", methods=["GET"])
def challenge1():
    return render_template("challenge1.html")


@app.route("/challenge2", methods=["GET"])
def challenge2():
    return render_template("challenge2.html")


@app.route("/challenge3", methods=["GET"])
def challenge3():
    return render_template("challenge3.html")


@app.route("/challenge4", methods=["GET"])
def challenge4():
    return render_template("challenge4.html")


@app.route("/challenge5", methods=["GET"])
def challenge5():
    return render_template("challenge5.html")


# Medium
@app.route("/challenge6", methods=["GET"])
def challenge6():
    return render_template("challenge6.html")


@app.route("/challenge7", methods=["GET"])
def challenge7():
    return render_template("challenge7.html")


@app.route("/challenge8", methods=["GET"])
def challenge8():
    return render_template("challenge8.html")


@app.route("/challenge9", methods=["GET"])
def challenge9():
    return render_template("challenge9.html")


@app.route("/challenge10", methods=["GET"])
def challenge10():
    return render_template("challenge10.html")


# Hard
@app.route("/challenge11", methods=["GET"])
def challenge11():
    source_cookie = request.cookies.get("source")

    response = make_response(render_template("challenge11.html"))

    if source_cookie is None:
        response = make_response(
            render_template("challenge11.html", src=request.remote_addr)
        )
        response.set_cookie(
            "source", value=request.remote_addr, max_age=604800, expires=None
        )
    else:
        source_cookie = source_cookie.replace('"', "&quot;")
        response = make_response(render_template("challenge11.html", src=source_cookie))

    return response


@app.route("/challenge12", methods=["GET", "POST"])
def challenge12():
    if request.method == "GET":
        if request.args.get("greeting"):
            greeting = "GET requests are blocked."
        else:
            greeting = "{{ greeting }}"
    elif request.method == "POST":
        if request.args.get("greeting"):
            greeting = request.args.get("greeting")
        else:
            greeting = "{{ greeting }}"

    return render_template("challenge12.html", greeting=greeting)


# Insane


@app.route("/challenge16", methods=["GET"])
def challenge16():
    if not request.args.get("url"):
        return redirect("/challenge16?url=/challenge1")
    url = request.full_path.split("?url=")[1]
    if url.startswith("/") or url.startswith("//"):
        pass
    elif not any(url.startswith(i) for i in ["https://", "javascript://"]):
        url = ""
    elif urlparse(url).netloc != request.headers["Host"]:
        url = ""

    url = unquote_plus(url)
    return render_template("challenge16.html", url=url)
