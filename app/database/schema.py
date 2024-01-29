async def create_database(cursor):
    try:
        await cursor.execute('''
            CREATE TABLE Users (    user_id BIGINT PRIMARY KEY AUTO_INCREMENT,    username VARCHAR(255) NOT NULL,    email VARCHAR(255) NOT NULL), ;
            CREATE TABLE Tweets (    tweet_id BIGINT PRIMARY KEY AUTO_INCREMENT,    user_id BIGINT,    content VARCHAR(280) NOT NULL,    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    FOREIGN KEY (user_id) REFERENCES Users(user_id));
            CREATE TABLE Comments (    comment_id BIGINT PRIMARY KEY AUTO_INCREMENT,    user_id BIGINT,    tweet_id BIGINT,    content VARCHAR(280) NOT NULL,    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    FOREIGN KEY (user_id) REFERENCES Users(user_id),    FOREIGN KEY (tweet_id) REFERENCES Tweets(tweet_id));
        ''')
    except:
        pass