import peewee
from configurations.database_connection import BaseModel


class Categoria_Produto(BaseModel):
    id_categoria = peewee.PrimaryKeyField()
    nome_categoria = peewee.CharField()
