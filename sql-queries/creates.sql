# drop database 471_project;

create database if not exists 471_project;

use 471_project;

# create Car table
create table if not exists car (
    vin_no int(32) not null,
    make varchar(100),
    model varchar(100),
    license_plate varchar(100) not null,
    status varchar(100),
    description varchar(250),
    primary key(vin_no)
);

# create Customer table
create table if not exists customer (
    license_no varchar(100) not null,
    phone_no varchar(100) not null,
    fname varchar(100) not null,
    lname varchar(100) not null,
    address varchar(250),
    email varchar(100),
    primary key(license_no)
);

# create User table
create table if not exists user (
    employee_no int(100) not null,
    phone_no varchar(100) not null,
    fname varchar(100) not null,
    lname varchar(100) not null,
    is_admin int(10) not null,
    address varchar(250),
    primary key(employee_no)
);

# create Event table
create table if not exists event (
    event_id int(32) not null auto_increment,
    car_vin int(32) not null,
    created_by int(100),
    description varchar(250) not null,
    title varchar(100) not null,
    status varchar(100),
    start_date date not null,
    end_date date,
    primary key(event_id),
    foreign key fk_vin(car_vin)
    references car(vin_no)
    on update cascade
    on delete cascade,
    foreign key fk_created_by(created_by)
    references user(created_by)
    on update cascade
    on delete set null
);

# note: no events should be created on their own, only with
# a corresponding backroom or pos event

# create POS table
create table if not exists pos (
    pos_id int(32) not null auto_increment,
    event_id int(32) not null,
    license_no varchar(100),
    primary key(pos_id),
    foreign key fk_license(license_no)
    references customer(license_no)
    on update cascade
    on delete set null,
    foreign key fk_event(event_id)
    references event(event_id)
    on update cascade
    on delete cascade
);

# create Backroom table
create table if not exists backroom (
    backroom_id int(32) not null auto_increment,
    event_id int(32) not null,
    assigned_to int(100),
    primary key(backroom_id),
    foreign key fk_event(event_id)
    references event(event_id)
    on update cascade
    on delete cascade,
    foreign key fk_assigned_to(assigned_to)
    references user(employee_no)
    on update cascade
    on delete set null

);

# POS sub tables

# create Rental table
create table if not exists rental (
    rental_id int(32) not null auto_increment,
    pos_id int(32) not null,
    problems varchar(25),
    est_return date,
    primary key(rental_id),
    foreign key fk_pos(pos_id)
    references pos(pos_id)
    on update cascade
    on delete cascade
);

# create Sale table
create table if not exists sale (
    sale_id int(32) not null auto_increment,
    pos_id int(32) not null,
    price int(100),
    primary key(sale_id),
    foreign key fk_pos(pos_id)
    references pos(pos_id)
    on update cascade
    on delete cascade
);

# create Available table
create table if not exists available (
    available_id int(32) not null auto_increment,
    pos_id int(32),
    backroom_id int(32),
    sale_price int(100),
    car_condition varchar(25),
    next_repair date,
    primary key(available_id),
    foreign key fk_pos(pos_id)
    references pos(pos_id)
    on update cascade
    on delete cascade,
    foreign key fk_backroom(backroom_id)
    references backroom(backroom_id)
    on update cascade
    on delete cascade
);

# Backroom sub tables

# create Writeoff table
create table if not exists writeoff (
    writeoff_id int(32) not null auto_increment,
    backroom_id int(32) not null,
    reason varchar(250),
    primary key(writeoff_id),
    foreign key fk_backroom(backroom_id)
    references backroom(backroom_id)
    on update cascade
    on delete cascade
);

# create Inspection table
create table if not exists inspection (
    inspection_id int(32) not null auto_increment,
    backroom_id int(32) not null,
    est_finish_date date,
    next_inspection date,
    work_done varchar(250),
    primary key(inspection_id),
    foreign key fk_backroom(backroom_id)
    references backroom(backroom_id)
    on update cascade
    on delete cascade
);

# create Repair table
create table if not exists repair (
    repair_id int(32) not null auto_increment,
    backroom_id int(32) not null,
    est_finish_date date,
    description varchar(250),
    parts_list varchar(250),
    primary key(repair_id),
    foreign key fk_backroom(backroom_id)
    references backroom(backroom_id)
    on update cascade
    on delete cascade
);

# Create Employee related tables

# create Agent table
create table if not exists agent (
    agent_id int(32) not null auto_increment,
    employee_no int(100) not null,
    total_sales int(100),
    primary key(agent_id),
    foreign key fk_employee(employee_no)
    references user(employee_no)
    on update cascade
    on delete cascade
);

# create Ratings table
create table if not exists rating (
    rating_id int(32) not null auto_increment,
    employee_no int(100) not null,
    rating int(100),
    primary key(rating_id),
    foreign key fk_employee(employee_no)
    references user(employee_no)
    on update cascade
    on delete cascade
);

# create Mechanic table
create table if not exists rating (
    mechanic_id int(32) not null auto_increment,
    employee_no int(100) not null,
    company varchar(250),
    speciality_list varchar(250),
    primary key(mechanic_id),
    foreign key fk_employee(employee_no)
    references user(employee_no)
    on update cascade
    on delete cascade
);

# not done: car colour, speciality, additional items

show tables;
