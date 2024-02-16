from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

users_database = {"churro": "pepepassword", "gnochhi": "gnocchipassword"}

# hashing values cheatsheet:
# import a hash function from hashlib module (sha1, for example)
# instantiate it: hash = sha1()
# update it: hash.update("potato".encode()) # notice encoding, it's mandatory
# get the hex digest with hash.hexdigest()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/static/style.css")
def css():
    return send_from_directory("files", "style.css")


app.run(debug=True)
