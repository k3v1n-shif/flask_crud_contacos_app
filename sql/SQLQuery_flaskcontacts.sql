-- Crear la base de datos
CREATE DATABASE flaskcontacts;

-- Usar la base de datos
USE flaskcontacts;

-- Crear la tabla contacts
CREATE TABLE contacts (
    id INT IDENTITY(1,1) PRIMARY KEY,
    fullname VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255)
);
