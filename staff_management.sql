CREATE DATABASE staff_management;

USE staff_management;

CREATE TABLE Address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    state VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20)
);

CREATE TABLE Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255),
    age INT,
    gender ENUM('Male', 'Female', 'Other'),
    salary DECIMAL(10, 2),
    address_id INT,
    FOREIGN KEY (address_id) REFERENCES Address(address_id)
);

USE staff_management;
SELECT * FROM Staff;
SELECT * FROM Address;

DELETE FROM Staff WHERE staff_id = 5;
DELETE FROM Address WHERE address_id = 5;

#create 
INSERT INTO Staff (full_name, age, gender, salary, address_id) 
VALUES ('Rupha', 30, 'Female', 55000.00, 1);

#update 
UPDATE Staff 
SET full_name = 'Rupha', age = 31, gender = 'Female', salary = 58000.00, address_id = 1 
WHERE staff_id = 1;

#delete
DELETE FROM Staff 
WHERE staff_id = 1;

#search for staff by name 
SELECT * FROM Staff 
WHERE full_name LIKE '%Rupha%';

#list all staff
SELECT * FROM Staff;


