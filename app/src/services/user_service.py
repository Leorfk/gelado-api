import logging
from repositories.usuario_repository import UsuarioRepository
from repositories.user_role_repository import UserRoleRepository
from models.usuario_model import UsuarioModel, UsuarioViewModel
from configurations.database_configuration import MysqlConnection


class UserService:

    def __init__(self,
                 user_repository: UsuarioRepository, role_repository: UserRoleRepository, db_conn: MysqlConnection) -> None:
        self.__user_repo = user_repository
        self.__role_repository = role_repository
        self.__db = db_conn

    def get_all_usuario(self):
        try:
            self.__db.reopen_connection()
            users = self.__db.execute_query_with_fetchall(
                self.__user_repo.select_all_usuario())
            if users:
                return self.to_array_view_model(users)
            else:
                return None
        except Exception as ex:
            return {'error': ex.args}
        finally:
            self.__db.close_connection()

    def get_usuario_by_id(self, id_user):
        try:
            self.__db.reopen_connection()
            query, params = self.__user_repo.select_usuario_by_id(id_user)
            usuario = self.__db.execute_query_with_fetchone(query, params)
            if usuario:
                return self.to_view_model(usuario)
            else:
                return None
        except Exception as ex:
            return {'error': ex.args}
        finally:
            self.__db.close_connection()

    def criar_usuario(self, role_name, usuario: UsuarioModel):
        try:
            self.__db.reopen_connection()
            role = self.buscar_role_por_nome(role_name)
            if role:
                query_user, params_user = self.__user_repo.insert_new_usuario(
                    usuario, role[0])
                user_id = self.__db.execute_query_with_lastrowid(
                    query_user, params_user)
                self.__db.commit_transaction()
                return {'message': f'Usuário cadastrado com sucesso',
                        'id': user_id,
                        'email': usuario.email}
            else:
                return {'error': f'role {role_name} não encontrada'}
        except Exception as ex:
            self.__db.rollback_transaction()
            return {'error': ex.args}
        finally:
            self.__db.close_connection()

    def delete_usuario(self, user_id):
        try:
            self.__db.reopen_connection()
            query, params = self.__user_repo.delete_usuario_by_id(user_id)
            if self.__db.execute_query_with_rowcount(query, params):
                self.__db.commit_transaction()
                return None
            else:
                return {'warnning': 'usuario inexistente'}
        except Exception as ex:
            return {'error': ex.args}
        finally:
            self.__db.close_connection()

    def atualizar_usuario(self, user_id, role_name, usuario: UsuarioModel):
        try:
            self.__db.reopen_connection()
            role = self.buscar_role_por_nome(role_name)
            if role:
                query, params = self.__user_repo.update_usuario_by_id(
                    usuario, role[0], user_id)
                if self.__db.execute_query_with_rowcount(query, params):
                    self.__db.commit_transaction()
                else:
                    return {'warnning': 'usuario não encontrado ou já atualizado com as informações'}
            else:
                return {'warnning': f'role {role_name} não cadastrada'}
        except Exception as ex:
            return {'error': ex.args}
        finally:
            self.__db.close_connection()

    def buscar_role_por_nome(self, role_name):
        query_role, params_role = self.__role_repository.select_user_role_by_texto_role(
            role_name)
        role = self.__db.execute_query_with_fetchone(query_role, params_role)
        return role

    def to_view_model(self, result_query: tuple):
        user = UsuarioViewModel(
            id_usuario=result_query[0], email=result_query[1], role_id=result_query[2])
        return user

    def to_array_view_model(self, result_set: list):
        return [self.to_view_model(user) for user in result_set]
