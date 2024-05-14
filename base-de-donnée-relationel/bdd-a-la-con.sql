DROP TABLE Membre;
DROP TABLE Groupe;
DROP TABLE Ami;
DROP TABLE Personne;

CREATE TABLE Personne(
    idpersonne NUMBER(10),
    nomPersonne VARCHAR2(30),
    age NUMBER(3),

    CONSTRAINT pk_personne PRIMARY KEY (idpersonne)
);

CREATE TABLE Ami(
    idpersonne1 NUMBER(10),
    idpersonne2 NUMBER(10),

    CONSTRAINT pk_ami PRIMARY KEY (idpersonne1,idpersonne2),

    CONSTRAINT fk1_ami FOREIGN KEY (idpersonne1) REFERENCES Personne(idpersonne),
    CONSTRAINT fk2_ami FOREIGN KEY (idpersonne2) REFERENCES Personne(idpersonne)
);

CREATE TABLE Groupe(
    idgroupe NUMBER(10),
    nomGroupe VARCHAR2(20),

    CONSTRAINT pk_groupe PRIMARY KEY (idgroupe)
);

CREATE TABLE Membre(
    idgroupe NUMBER(10),
    idpersonne NUMBER(10),

    CONSTRAINT pk_membre PRIMARY KEY (idGroupe,idpersonne),

    CONSTRAINT fk1_membre FOREIGN KEY (idgroupe) REFERENCES Groupe(idgroupe),
    CONSTRAINT fk2_membre FOREIGN KEY (idpersonne) REFERENCES Personne(idpersonne)
);
