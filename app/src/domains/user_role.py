class UserRole:

    def __init__(self, id_role, tipo_role) -> None:
        self.__id_role = id_role
        self.__texto_role = tipo_role

    @property
    def id_role(self):
        return self.__id_role

    @property
    def texto_role(self):
        return self.__texto_role
