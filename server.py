# 0. import flask
from flask import Flask

# 1. create the flask application
app = Flask("app")

# 2. create a route
@app.route("/")
def index():
    return """
    <h1>Hello from Flask</h1>
    <h2><a href="/login">go to login</a></h2>
    """

@app.route("/login")
def login():
    return """
    <h1>please login!</h1>
    <h2><a href="/">go back home</a></h2>
    """

# 3. run the application
app.run()
