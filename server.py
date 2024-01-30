# 0. import flask
from flask import Flask, jsonify

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

@app.route("/sneakers/<sneaker_id>", methods=["GET"])
def sneaker_1(sneaker_id):
    name = None
    if sneaker_id == "1":
        name = "Air Force"
    elif sneaker_id == "2":
        name = "Sambas"

    return f"""
    <h1>{name}</h1>
    <h2><a href="/">go back home</a></h2>
    """

@app.route("/api/salute/<name>/<int:age>/<str:course>")
def salute(name, age, course):
    return jsonify({"message": f"Hello {name}, with {age} years of age from {course} course"})

# 3. run the application
app.run()
