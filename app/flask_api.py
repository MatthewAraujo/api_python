
from flask import Flask, request, jsonify, render_template,url_for,redirect,send_file
from os import getcwd
import database.mysql_provider as mysql_provider
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

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
    mysql.query("INSERT INTO Tweets (user_id, content) VALUES ((SELECT user_id FROM Users WHERE username = %s), %s)", (userId, content))
    return jsonify(data)

@app.route("/tweet", methods=['GET'])
def api_get_tweet():
    mysql = mysql_provider.MySQL()
    data = mysql.query("SELECT tweet_id, username, content, timestamp FROM Tweets T INNER JOIN Users U ON T.user_id = U.user_id ORDER BY timestamp DESC;")
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

@app.route("/dump", methods=['GET'])
def api_get_dump():
    mysql = mysql_provider.MySQL()
    data = mysql.dump()
    with open("dump.txt", "w", encoding="utf-8") as f:
        count = 0
        for line in data:
            if count==0:
                line = "User.user_id,User.username,User.email,Tweet.tweet_id,Tweet.content,Tweet.timestamp,Comment.comment_id,Comment.content,Comment.timestamp".split(",")
            line = ','.join(map(str, line))
            f.write(line)
            f.write("\n")
            count+=1
    path = getcwd()+"/dump.txt"
    return send_file(path, as_attachment=True)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))