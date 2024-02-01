from flask import Flask, send_from_directory
import sys

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/logo")
def image():
    return send_from_directory("images", "flask.jpg")


app.run(debug=True)
