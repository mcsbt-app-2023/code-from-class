from flask import Flask, render_template

app = Flask(__name__)

beatles = [
    "John",
    "George",
    "Ringo",
    "Paul",
]


@app.route("/")
def index():
    render_band = True
    return render_template("beatles.html", band=beatles)


app.run(debug=True)
