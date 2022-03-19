from models import categoria_produto_model, produto_model
import peewee
if __name__ == '__main__':
    pass
    # xap = categoria_produto_model.Categoria_Produto.create(
    #     id_categoria=1, nome_categoria='Toma_7')
    # print(xap)
    # toma = produto_model.Produto.create(
    #     id_produto=None,
    #     nome='Gulosinho',
    #     descricao='mamada',
    #     preco=120.00,
    #     categoria_id=1
    # )
    # try:
    #     categoria_produto_model.Categoria_Produto.create_table()
    #     print('funfo')
    # except peewee.OperationalError as ex:
    #     print(ex)
    # try:
    #     produto_model.Produto.create_table()
    #     print('funfo')
    # except peewee.OperationalError as ex:
    #     print(ex)
