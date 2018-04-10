use 471_project;

# example car insert
insert into car(
vin_no,
make,
model,
license_plate
) 
values(
123456,
"ford",
"f150",
"T2R123"
);

# example customer insert
insert into customer(
license_no,
phone_no,
fname,
lname
) 
values(
"12FG992",
"5871231234",
"John",
"Doe"
);

# example user insert
insert into user(
employee_no,
phone_no,
fname,
lname,
is_admin
) 
values(
2345223,
"5871231234",
"Jimmy",
"Doe",
1
);

# cars
insert into car(vin_no, make, license_plate) values(459827, "chevrolet", "RF2319");

insert into car(vin_no, make, model, license_plate) values (32145, "toyota", "corolla", "P238NM");

