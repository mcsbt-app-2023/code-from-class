from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", year=2124)


@app.route("/about")
def about():
    return send_from_directory("files", "about.html")


@app.route("/login")
def login():
    return send_from_directory("files", "login.html")


@app.route("/static/style.css")
def css():
    return send_from_directory("files", "style.css")


app.run(debug=True)
