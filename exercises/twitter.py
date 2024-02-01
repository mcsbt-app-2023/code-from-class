from flask import Flask, request

tweets_database = []

# Create a route to receive new tweets and store them in our _database_
# and another route to list all tweets
app = Flask(__name__)


@app.route("/tweet", methods=["PUT"])
def post_tweet():
    tweet = request.get_json()

    tweets_database.append(tweet)

    return "tweet posted", 201


@app.route("/", methods=["GET"])
def index():
    body = "<ul>"

    for tweet in tweets_database:
        body += "<li>" + tweet["content"] + "</li>"

    body += "</ul>"
    return body, 200


app.run()
