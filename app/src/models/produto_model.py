import peewee
from configurations.database_connection import BaseModel
from models.categoria_produto_model import Categoria_Produto


class Produto(BaseModel):
    id_produto = peewee.PrimaryKeyField()
    nome = peewee.CharField()
    descricao = peewee.CharField()
    preco = peewee.DecimalField(max_digits=17, decimal_places=2)
    categoria_id = peewee.ForeignKeyField(Categoria_Produto)
