-- docker run -d --name gelado-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql

drop database if exists gelado;

create database if not exists gelado;
use gelado;
create table if not exists user_role
(
    id_role integer primary key,
    texto_role varchar(100) unique
);
create table if not exists usuario
(
    id_usuario integer primary key auto_increment,
    email varchar(100) unique,
    senha varchar(1000),
    role_id integer
);

create table if not exists cliente
(
    id_cliente integer primary key auto_increment,
    nome varchar(200),
    cpf_cnpj varchar(14),
    usuario_id integer
);

create table if not exists telefone
(
    id_telefone integer primary key auto_increment,
    numero_telefone varchar(14),
    usuario_id integer
);

create table if not exists endereco
(
    id_endereco integer primary key auto_increment,
    municipio varchar(100),
    bairro varchar(100),
    nome_rua varchar(100),
    numero integer,
    cep varchar(9),
    usuario_id integer
);

create table if not exists pedido
(
    id_pedido integer primary key auto_increment,
    data_pedido timestamp,
    cliente_id integer
);

create table if not exists item_pedido
(
    id_item_pedido integer primary key auto_increment,
    quantidade integer,
    valor_item_pedido decimal(17,2),
    pedido_id integer,
    produto_id integer
);

create table if not exists produto
(
    produto_id integer primary key auto_increment,
    nome varchar(100),
    preco decimal(17,2),
    descricao varchar(500),
    categoria_id integer
);

create table if not exists categoria_produto
(
    id_categoria integer primary key auto_increment,
    nome_categoria varchar(100) unique
);

/*criacao as fks*/

alter table usuario add constraint fk_usuario_role foreign key (role_id) references user_role (id_role);

alter table cliente add constraint fk_cliente_usuario foreign key (usuario_id) references usuario (id_usuario);

alter table telefone add constraint fk_telefone_usuario foreign key (usuario_id) references usuario (id_usuario);

alter table endereco add constraint fk_endereco_usuario foreign key (usuario_id) references usuario (id_usuario);

alter table pedido add constraint fk_pedido_cliente foreign key (cliente_id) references cliente (id_cliente);

alter table item_pedido add constraint fk_item_pedido_pedido foreign key (pedido_id) references pedido (id_pedido);

alter table item_pedido add constraint fk_item_pedido_produto foreign key (produto_id) references produto (produto_id);

alter table produto add constraint fk_produto_categoria foreign key (categoria_id) references categoria_produto (id_categoria);