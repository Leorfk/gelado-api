import peewee
from configurations.database_connection import BaseModel

class User_Role(BaseModel):
    id_role = peewee.PrimaryKeyField()
    texto_role = peewee.CharField(unique=True)