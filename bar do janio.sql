create database if not exists bar;

create schema if not exists bar;

use bar;

show databases;

-- CRIANDO AS TABELAS

create table if not exists bar.customer(
	id INT not null auto_increment,
    order_ammount INT not null,
    primary key(id)
);

create table if not exists bar.roleBar(
	id INT not null auto_increment,
    description_role varchar(256) not null,
    name_role varchar(45) not null,
    primary key(id)
);

create table if not exists bar.employee(
	id INT not null auto_increment,
    salary decimal(2) not null,
    primary key(id),
    foreign key(id) references bar.roleBar(id)
    
);

create table if not exists bar.person(
	id INT not null auto_increment,
    person_name varchar(256) not null,
    cpf char(11) not null,
    rg varchar(11) not null,
    phone varchar(20) not null,
    mail varchar(45) not null,
    unique(cpf),
    primary key(id),
    foreign key(id) references bar.customer(id),
    foreign key(id) references bar.employee(id)
);

create table if not exists bar.bar(
	id INT not null auto_increment,
    bar_name varchar(45) not null,
    phone varchar(20) not null,
    mail varchar(45) not null,
    primary key(id)
);

create table if not exists bar.billing(
	id INT not null auto_increment,
    value_billing decimal(2) not null,
    date_billing DATE not null,
    status_billing tinyint(1) not null,
    primary key(id),
    foreign key(id) references bar.methodOfPayment(id)
);

create table if not exists bar.sale(
	id INT not null auto_increment,
    date_sale DATE not null,
    creation_date datetime not null,
    primary key(id),
    foreign key(id) references bar.customer(id),
    foreign key(id) references bar.billing(id),
    foreign key(id) references bar.employee(id)
);

create table if not exists bar.orderBar(
	id INT not null auto_increment,
    quantity INT not null,
    value_order decimal(2) not null,
    primary key(id),
    foreign key(id) references bar.employee(id),
    foreign key(id) references bar.sale(id)
);

create table if not exists bar.payment(
	id INT not null auto_increment,
    value_payment decimal(2) not null,
    description_payment varchar(256) not null,
    name_payment varchar(45) not null,
    primary key(id),
    foreign key(id) references bar.employee(id)
);

create table if not exists bar.product(
	id INT not null auto_increment,
    value_product decimal(2) not null,
    name_product varchar(45) not null,
    description_product varchar(256) not null,
    primary key(id),
    foreign key(id) references bar.employee(id),
    foreign key(id) references bar.orderBar(id),
    foreign key(id) references bar.sale(id)
);

create table if not exists bar.evaluation(
	id INT not null auto_increment,
	comment_evaluation varchar(100),
    rating tinyint(5) not null,
    date_evaluation DATE not null,
    primary key(id),
    foreign key(id) references bar.customer(id),
    foreign key(id) references bar.bar(id)
);

create table if not exists bar.methodOfPayment(
	id INT not null auto_increment,
    name_method varchar(45) not null,
    description_method varchar(256) not null,
    primary key(id),
	foreign key(id) references bar.billing(id)
);

    

    
    
    
    
    
