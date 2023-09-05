drop database bar;
create database if not exists bar;

drop schema bar;
create schema if not exists bar;

use bar;

show databases;

-- CRIANDO AS TABELAS

drop table if exists bar.person;

create table if not exists bar.person(
	id INT not null auto_increment,
    person_name varchar(256) not null,
    cpf char(11) not null,
    rg varchar(11) not null,
    birth_date date not null,
    unique(cpf),
    primary key(id)
);

drop table if exists bar.customer;

create table if not exists bar.customer(
	id INT not null auto_increment,
    order_ammount INT not null,
    primary key(id),
    foreign key(id) references bar.person(id)
);

create table if not exists bar.bar(
	id INT not null auto_increment,
    bar_name varchar(45) not null,
    phone varchar(12) not null,
    mail varchar(45) not null,
    primary key(id)
);

create table if not exists bar.employee(
	id INT not null auto_increment,
    salary decimal(2) not null,
    primary key(id)
);

create table if not exists bar.roleBar(
	id INT not null auto_increment,
    description_role varchar(256) not null,
    name_role varchar(45) not null,
    primary key(id)
);

create table if not exists bar.sale(
	id INT not null auto_increment,
    date_sale DATE not null,
    primary key(id)
);

create table if not exists bar.orderBar(
	id INT not null auto_increment,
    qtde INT not null,
    value_order decimal(2) not null,
    primary key(id)
);

create table if not exists bar.payment(
	id INT not null auto_increment,
    value_payment decimal(2) not null,
    description_payment varchar(256) not null,
    name_payment varchar(45) not null,
    primary key(id)
);

create table if not exists bar.product(
	id INT not null auto_increment,
    value_product decimal(2) not null,
    name_product varchar(45) not null,
    description_product varchar(256) not null,
    primary key(id)
);

create table if not exists bar.evaluation(
	id INT not null auto_increment,
	comment_evaluation varchar(100),
    rating tinyint(5) not null,
    date_evaluation DATE not null,
    primary key(id),
    foreign key(id) references bar.customer(id)
);

create table if not exists bar.billing(
	id INT not null auto_increment,
    value_billing decimal(2) not null,
    date_billing DATE not null,
    status_billing tinyint(1) not null,
    primary key(id)
);

create table if not exists bar.methodOfPayment(
	id INT not null auto_increment,
    name_method varchar(45) not null,
    description_method varchar(256) not null,
    primary key(id)
);


    

    
    
    
    
    
