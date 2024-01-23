from db import connection,MySQLdb

class MySQL:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def query(self, sql, *args):
        self.cursor.execute(sql,*args)
        self.connection.commit()
        self.connection.close()
        return self.cursor.fetchall()
    
    

   