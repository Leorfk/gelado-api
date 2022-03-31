from configurations.database_configuration import MysqlConnection
class DatabaseRepository:

    def __init__(self, db_connection: MysqlConnection):
        self.db_connection = db_connection
        self.conn = self.db_connection.create_connection()
        print('conectou')

    def execute_query(self, query: str, params: tuple):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        cursor.close()
    
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