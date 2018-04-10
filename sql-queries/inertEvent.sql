use 471_project;

#example event insert
insert into event(car_vin, created_by, description, title, status, start_date, end_date) values (32145, 2345223, "This is a description", "This is a title", "This is a status",  '1992-02-25', '1993-02-25');

insert into event(car_vin, created_by, description, title, status, start_date, end_date) values (459827, 2345223, "This is also description", "This is also title", "This is also status",  '1992-02-25', '1993-02-25');

insert into user(employee_no, phone_no, fname, lname, is_admin) values (123123, "18002472001", "Jane", "Doe", 0);
