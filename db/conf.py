import pymysql # ignore it


class ConnectionConfig:
    instance = None
    connection = None
    cursor = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.connection = pymysql.connect(
                host='127.0.0.1',
                user='my_user',
                password='3212#Moya3212',
                db='Recipes',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            cls.cursor = cls.connection.cursor()
        return cls.instance

    
    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

        return self.cursor.description

    
    def close(self):
        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None:
            self.connection.close()

