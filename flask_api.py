
from flask import Flask, request, jsonify
import mysql_provider
app = Flask(__name__)	
@app.route('/user', methods=['POST'])
def api_post():
    data = request.get_json()
    mysql = mysql_provider.MySQL()
    mysql.query("INSERT INTO Users (username,email) VALUES ('{}', '{}');".format(data["username"], data['email']))
    return jsonify(data)

@app.route('/user', methods=['GET'])
def api_get():
    mysql = mysql_provider.MySQL()
    data = mysql.query("SELECT * FROM Users;")
    return jsonify(data)

@app.route('/user/<int:user_id>', methods=['GET'])
def api_get_user(user_id):
    mysql = mysql_provider.MySQL()
    data = mysql.query("SELECT * FROM Users WHERE user_id = {};".format(user_id))
    return jsonify(data)

@app.route("/tweet", methods=['POST'])
def api_post_tweet():
    data = request.get_json()
    userId = data["user_id"]
    content = data["content"]
    mysql = mysql_provider.MySQL()
    mysql.query("INSERT INTO Tweets (user_id,content) VALUES(%s,%s);", (userId, content))
    return jsonify(data)

@app.route("/tweet", methods=['GET'])
def api_get_tweet():
    mysql = mysql_provider.MySQL()
    data = mysql.query("SELECT * FROM Tweets;")
    return jsonify(data)

@app.route("/tweet/<int:tweet_id>", methods=['GET'])
def api_get_tweet_id(tweet_id):
    mysql = mysql_provider.MySQL()
    data = mysql.query("SELECT * FROM Tweets WHERE tweet_id = {};".format(tweet_id))
    return jsonify(data)

@app.route("/comment", methods=['POST'])
def api_post_comment():
    data = request.get_json()
    userId = data["user_id"]
    tweetId = data["tweet_id"]
    content = data["content"]
    mysql = mysql_provider.MySQL()
    mysql.query("INSERT INTO Comments (user_id,tweet_id,content) VALUES(%s,%s,%s);", (userId, tweetId, content))
    return jsonify(data)

@app.route("/comment", methods=['GET'])
def api_get_comment():
    mysql = mysql_provider.MySQL()
    data = mysql.query("SELECT * FROM Comments;")
    return jsonify(data)

@app.route("/comment/<int:comment_id>", methods=['GET'])
def api_get_comment_id(comment_id):
    mysql = mysql_provider.MySQL()
    data = mysql.query("SELECT * FROM Comments WHERE comment_id = {};".format(comment_id))
    return jsonify(data)