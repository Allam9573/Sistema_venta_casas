create database db_casas;
use db_casas;
create table casas(
	id int primary key auto_increment,
    direccion varchar(100) not null,
    precio decimal(10,2) not null
);