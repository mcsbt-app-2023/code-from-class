from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello", 200

@app.route("/notfound")
def notfound():
    return "this resource is not found", 404

app.run()