# 0. import flask
from flask import Flask

# 1. create the flask application
app = Flask("app")

# 2. create a route
@app.route("/")
def index():
    return "<h1>Hello from Flask</h1>"

# 3. run the application
app.run()
