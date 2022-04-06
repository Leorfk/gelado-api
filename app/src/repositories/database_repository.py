from configurations.database_configuration import MysqlConnection


class DatabaseRepository:

    def __init__(self, db_connection: MysqlConnection):
        self.db_connection = db_connection
        self.conn = self.db_connection.create_connection()
        print('conectou')

    def execute_query(self, query: str, params: tuple = None, commit=False):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        cursor.close()
        if commit:
            self.conn.commit()

    def execute_query_with_rowcount(self, query: str, params: tuple = None, commit=False):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.rowcount
        cursor.close()
        if commit:
            self.conn.commit()
        return result

    def execute_query_with_fetchall(self, query: str, params: tuple = None, commit=False):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        if commit:
            self.conn.commit()
        return result

    def execute_query_with_fetchone(self, query: str, params: tuple = None, commit=False):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        if commit:
            self.conn.commit()
        return result

    def delete_any(self, table):
        query = f'delete from {table}'
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.close()

    def commit_changes(self):
        self.conn.commit()

    def get_connection(self):
        self.conn = self.db_connection.create_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.conn.close()
            print('fechou')

    def rollback(self):
        self.conn.rollback()
