from pydantic import BaseModel, validator
from typing import List

# user role service
class UserRoleModel(BaseModel):
    id_role: int
    texto_role: str

# user service
class UsuarioViewModel(BaseModel):
    id_usuario: int
    email: str
    role_id: int


class UsuarioModel(BaseModel):
    email: str
    senha: str

# cliente service
class TelefoneModel(BaseModel):
    numero_telefone: str


class EnderecoModel(BaseModel):
    municipio: str
    bairro: str
    nome_rua: str
    cep: str
    numero: int


class ClienteModel(BaseModel):
    nome: str
    cpf_cnpj: str

class UsuarioRealOficialModel(BaseModel):
    user: UsuarioModel
    user_role: UserRoleModel
    cliente: ClienteModel
    telefones: List[TelefoneModel]
    endereco: EnderecoModel