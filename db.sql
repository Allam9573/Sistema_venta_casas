create database db_casas;
use db_casas;
create table casas(
	id int primary key auto_increment,
    direccion varchar(100) not null,
    propietario varchar(100) not null,
    precio decimal(10,2) not null,
    foto varchar(100) not null
);
drop table usuarios;
create table usuarios(
    id int primary key auto_increment,
    nombre varchar(100) not null,
    correo varchar(100) not null,
    usuario varchar(100) not null,
    contrasenia text not null
);
select * from usuarios;