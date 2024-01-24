from database.db import connection

class MySQL:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def query(self, sql, *args):
        self.cursor.execute(sql,*args)
        self.connection.commit()
        return self.cursor.fetchall()
    
    def dump(self):
        self.cursor.execute("SELECT     Users.user_id,    Users.username,    Users.email,    Tweets.tweet_id,    Tweets.content AS tweet_content,    Tweets.timestamp AS tweet_timestamp,    Comments.comment_id,    Comments.content AS comment_content,    Comments.timestamp AS comment_timestamp FROM Users LEFT JOIN Tweets ON Users.user_id = Tweets.user_id LEFT JOIN Comments ON Tweets.tweet_id = Comments.tweet_id;")
        return self.cursor.fetchall()
    
    

   