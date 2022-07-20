import mysql.connector


class MysqlConnection:

    def create_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="gelado"
        )
