class DatabaseRepository:

    def _execute_query(self, cursor, query: str, params: tuple = None):
        cursor.execute(query, params)

    def _execute_query_with_rowcount(self, cursor, query: str, params: tuple = None):
        cursor.execute(query, params)
        result = cursor.rowcount
        return result

    def _execute_query_with_lastrowid(self, cursor, query: str, params: tuple = None):
        cursor.execute(query, params)
        result = cursor.lastrowid
        return result

    def _execute_query_with_fetchall(self, cursor, query: str, params: tuple = None):
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result

    def _execute_query_with_fetchone(self, cursor, query: str, params: tuple = None):
        cursor.execute(query, params)
        result = cursor.fetchone()
        return result

    def _delete_any(self, cursor, table):
        query = f'delete from {table}'
        cursor.execute(query)
