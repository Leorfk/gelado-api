from repositories.user_role_repository import UserRoleRepository
from models.usuario_model import UserRoleModel
from repositories.database_repository import MysqlConnection


class UserRoleService:

    def __init__(self,
                 user_repository: UserRoleRepository, db_conn: MysqlConnection) -> None:
        self.__repository = user_repository
        self.__db = db_conn

    def get_role_by_id(self, role_id):
        try:
            self.__db.reopen_connection()
            query, params = self.__repository.select_user_role_by_id_role(
                role_id)
            role = self.__db.execute_query_with_fetchone(query, params)
            if role:
                return self.to_model(role)
            else:
                return None
        except Exception as ex:
            return {'error': ex}
        finally:
            self.__db.close_connection()

    def get_all_user_role(self):
        try:
            self.__db.reopen_connection()
            result = self.__db.execute_query_with_fetchall(
                self.__repository.select_all_user_role())
            if result:
                return self.to_array_model(result)
            else:
                return None
        except Exception as ex:
            return {'error': ex}
        finally:
            self.__db.close_connection()

    def create_user_role(self, user_role: UserRoleModel):
        try:
            self.__db.reopen_connection()
            query, params = self.__repository.insert_new_user_role(user_role)
            self.__db.execute_query(query, params)
            self.__db.commit_transaction()
            return {'message': f'Role cadastrada com sucesso: {user_role.texto_role}'}
        except Exception as ex:
            self.__db.rollback_transaction()
            return {'error': ex.args}
        finally:
            self.__db.close_connection()

    def delete_role_by_id(self, role_id):
        try:
            self.__db.reopen_connection()
            query, params = self.__repository.delete_role_by_id_role(
                self.__db.cursor, role_id)
            return self.__db.execute_query_with_rowcount(query, params)
        except Exception as ex:
            return {'error': ex.args}
        finally:
            self.__db.close_connection()

    def to_model(self, result: tuple):
        return UserRoleModel(id_role=result[0], texto_role=result[1])

    def to_array_model(self, result_set: list):
        return [self.to_model(r) for r in result_set]
