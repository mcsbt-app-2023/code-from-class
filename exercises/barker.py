from flask import (
    Flask,
    send_from_directory,
    render_template,
    request,
    session,
    redirect,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "something very secret"

users_database = {
    "churro": "ab5743ce10dcb8eec8eba72e2aae97f684891786",
    "gnocchi": "0adbe085fd8eb9a6ace9300130d5d3f6ff0baf22",
}

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


@app.route("/handle-login", methods=["POST"])
def handle_login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users_database and users_database[username] == password:
        session["username"] = username
        return redirect("/")
    else:
        return redirect("/register")


@app.route("/static/style.css")
def css():
    return send_from_directory("files", "style.css")


app.run(debug=True)
