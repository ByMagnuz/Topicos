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
INSERT INTO Entidad_Federativa (nombre) VALUES ('Ciudad de México');
INSERT INTO Entidad_Federativa (nombre) VALUES ('Estado de México');
INSERT INTO Entidad_Federativa (nombre) VALUES ('Jalisco');

-- Insertar datos en Municipio
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Cuauhtémoc', 1);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Iztapalapa', 1);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Toluca', 2);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Ecatepec', 2);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Guadalajara', 3);
INSERT INTO Municipio (nombre, id_entidad) VALUES ('Zapopan', 3);

-- Insertar datos en Destinatario
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Juan Pérez', 'Calle Reforma 123, Cuauhtémoc, CDMX', 1);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('María López', 'Avenida Tláhuac 456, Iztapalapa, CDMX', 2);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Carlos García', 'Boulevard Aeropuerto 789, Toluca, Estado de México', 3);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Ana Martínez', 'Calle Juárez 1011, Ecatepec, Estado de México', 4);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Luis Hernández', 'Avenida Vallarta 1213, Guadalajara, Jalisco', 5);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Laura González', 'Calle Patria 1415, Zapopan, Jalisco', 6);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Miguel Ramírez', 'Calle Insurgentes 1617, Cuauhtémoc, CDMX', 1);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Sofía Torres', 'Avenida Ermita 1819, Iztapalapa, CDMX', 2);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Pedro Sánchez', 'Calle Hidalgo 2021, Toluca, Estado de México', 3);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Lucía Flores', 'Boulevard de los Aztecas 2223, Ecatepec, Estado de México', 4);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Diego Fernández', 'Avenida Circunvalación 2425, Guadalajara, Jalisco', 5);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Valeria Ruiz', 'Calle López Mateos 2627, Zapopan, Jalisco', 6);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('José Gómez', 'Calle División del Norte 2829, Cuauhtémoc, CDMX', 1);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Carmen Castillo', 'Avenida Central 3031, Iztapalapa, CDMX', 2);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Raúl Moreno', 'Boulevard Solidaridad 3233, Toluca, Estado de México', 3);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Gloria Núñez', 'Calle Venustiano Carranza 3435, Ecatepec, Estado de México', 4);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Felipe Jiménez', 'Avenida México 3637, Guadalajara, Jalisco', 5);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Gabriela Vargas', 'Calle Américas 3839, Zapopan, Jalisco', 6);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Hugo Ramírez', 'Calle Morelos 4041, Cuauhtémoc, CDMX', 1);
INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('Patricia Salazar', 'Avenida Zaragoza 4243, Iztapalapa, CDMX', 2);