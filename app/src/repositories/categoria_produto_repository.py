from models.categoria_produto_model import Categoria_Produto


class CategoriaProdutoRepository:
    def __init__(self, database: Categoria_Produto) -> None:
        self.__categoria_produto_model = database

    def create_categoria_produto(self):
        pass

    def delete_categoria_produto(self, id_categoria_produto: int):
        pass

    def update_categoria_produto(self):
        pass

    def get_all_categoria_produto(self):
        pass

    def get_categoria_produto_by_id(self, id_categoria_produto: int):
        pass
