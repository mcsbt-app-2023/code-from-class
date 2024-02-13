from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    logged_in = True
    return render_template("loggedin.html")


app.run(debug=True)
