-- Crear base de datos
CREATE DATABASE IF NOT EXISTS ProyectoTop;
USE ProyectoTop;

-- Crear tabla Entidad_Federativa
CREATE TABLE IF NOT EXISTS Entidad_Federativa (
    id_entidad INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);

-- Crear tabla Municipio
CREATE TABLE IF NOT EXISTS Municipio (
    id_municipio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_entidad INT NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_entidad) REFERENCES Entidad_Federativa(id_entidad)
);

-- Crear tabla Destinatario
CREATE TABLE IF NOT EXISTS Destinatario (
    id_destinatario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    id_municipio INT NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_municipio) REFERENCES Municipio(id_municipio)
);

-- Insertar datos en Entidad_Federativa
INSERT INTO Entidad_Federativa (nombre) VALUES ('Entidad A');
INSERT INTO Entidad_Federativa (nombre) VALUES ('Entidad B');
INSERT INTO Entidad_Federativa (nombre) VALUES ('Entidad C');

-- Insertar datos en Municipio
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Municipio A1', 1);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Municipio A2', 1);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Municipio B1', 2);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Municipio B2', 2);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Municipio C1', 3);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Municipio C2', 3);

-- Insertar datos en Destinatario
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Destinatario 1', 'Calle Falsa 123', 1);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Destinatario 2', 'Calle Verdadera 456', 2);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Destinatario 3', 'Avenida Siempreviva 789', 3);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Destinatario 4', 'Boulevard Ficticio 1011', 4);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Destinatario 5', 'Calle Imaginaria 1213', 5);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Destinatario 6', 'Avenida Inventada 1415', 6);