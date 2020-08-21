CREATE DATABASE IF NOT EXISTS discordbot;

USE discordbot; 

CREATE TABLE Members (
    idUser INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    User VARCHAR (200) NOT NULL,
    Points INTEGER NOT NULL, 
    idRoles INTEGER,
    FOREIGN KEY (idRoles) REFERENCES Roles (idRoles)
);

CREATE TABLE Questions (
    idMensaje INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Question VARCHAR (200) NOT NULL, 
    idUser INTEGER NOT NULL,
    FOREIGN KEY (idUser) REFERENCES Members (idUser)
);

CREATE TABLE Answers (
    idMensaje INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Answer VARCHAR (200) NOT NULL, 
    idUser INTEGER NOT NULL,
    FOREIGN KEY (idUser) REFERENCES Members (idUser)
);

CREATE TABLE Roles (
    idRoles INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Roles VARCHAR (200) NOT NULL
);


--Agregando datos para los roles.
INSERT INTO Roles (Roles) VALUES  ('Primaria');
INSERT INTO Roles (Roles) VALUES  ('Secundaria');
INSERT INTO Roles (Roles) VALUES  ('Preuniversitario');
INSERT INTO Roles (Roles) VALUES  ('Universitario');
INSERT INTO Roles (Roles) VALUES  ('Mentor');

--Agregando datos para los miembros.
INSERT INTO Members (User, Codeuser, Points, idRoles) VALUES (
    'Empire', '#9240', 0, 5
);
INSERT INTO Members (User, Codeuser, Points, idRoles) VALUES (
    'Bleak', '#1234', 0, 5
);
INSERT INTO Members (User, Codeuser, Points, idRoles) VALUES (
    'Grich', '#7631', 0, 2
);
INSERT INTO Members (User, Codeuser, Points, idRoles) VALUES (
    'Messi', '#8100', 0, 4
);

--Agregando Preguntas.
INSERT INTO Questions (Question, idUser) VALUES (
    '¿Porqué tres puntos en un mismo plano forman un triángulo?', 3
);
INSERT INTO Questions (Question, idUser) VALUES (
    '¿Primero fue el huevo o la gallina?', 4
);
INSERT INTO Questions (Question, idUser) VALUES (
    '¿Cuál es el significado de la vida?', 3
);
INSERT INTO Questions (Question, idUser) VALUES (
    'Necesito tips para mejorar la concentración', 2
);
INSERT INTO Questions (Question, idUser) VALUES (
    '¿Cómo dejo de procastinar?', 1
);

