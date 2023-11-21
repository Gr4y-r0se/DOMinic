from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-256-bit-secret"

from modules import *


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port="443",
        ssl_context=("certificates/cert.pem", "certificates/key.pem"),
        debug=False,
    )
