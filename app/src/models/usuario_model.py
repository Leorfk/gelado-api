import peewee
from configurations.database_connection import BaseModel
from models.user_role_model import User_Role


class Usuario(BaseModel):
    id_usuario = peewee.PrimaryKeyField()
    email = peewee.CharField()
    senha = peewee.CharField()
    role_id = peewee.ForeignKeyField(User_Role)
