from models.produto_model import Produto


class ProdutoRepository:
    def __init__(self, database: Produto) -> None:
        self.__produto_model = database

    def create_produto(self):
        pass

    def delete_produto(self, id_produto: int):
        pass

    def update_produto(self):
        pass

    def get_all_produto(self):
        pass

    def get_produto_by_id(self, id_produto: int):
        pass
