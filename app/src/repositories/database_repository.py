import mysql.connector


class MysqlConnection:

    def __init__(self) -> None:
        self.conn, self.cursor = self.__get_resources()

    def __get_resources(self) -> None:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="gelado"
        )
        cursor = conn.cursor()
        return conn, cursor

    def close_connection(self) -> None:
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()

    def reopen_connection(self) -> None:
        if self.conn is None:
            self.conn, self.cursor = self.__get_resources()
        elif self.conn.is_connected() is False:
            self.conn, self.cursor = self.__get_resources()

    def commit_transaction(self) -> None:
        self.conn.commit()

    def rollback_transaction(self) -> None:
        self.conn.rollback()

    def execute_query(self, query: str, params: tuple = None) -> None:
        self.cursor.execute(query, params)

    def execute_query_with_rowcount(self, query: str, params: tuple = None) -> int:
        self.cursor.execute(query, params)
        result = self.cursor.rowcount
        return result

    def execute_query_with_lastrowid(self, query: str, params: tuple = None) -> int:
        self.cursor.execute(query, params)
        result = self.cursor.lastrowid
        return result

    def execute_query_with_fetchall(self, query: str, params: tuple = None) -> list:
        self.cursor.execute(query, params)
        result = self.cursor.fetchall()
        return result

    def execute_query_with_fetchone(self, query: str, params: tuple = None) -> tuple:
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        return result
