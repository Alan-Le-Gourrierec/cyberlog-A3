-------- creation des tables
CREATE TABLE Personne( 
	id_personne NUMBER(20), 
 	nom_personne VARCHAR2(25), 
 	age NUMBER(3), 
 	CONSTRAINT pk1 PRIMARY KEY (id_personne));
 
 
 CREATE TABLE Ami( 
  	id_personne1 NUMBER(20), 
  	id_personne2 NUMBER(20), 
	CONSTRAINT pk2 PRIMARY KEY (id_personne1,id_personne2), 
	CONSTRAINT fk1 FOREIGN KEY (id_personne1) REFERENCES Personne(id_personne), 
  	CONSTRAINT fk2 FOREIGN KEY (id_personne2) REFERENCES Personne(id_personne));
  	
  	CREATE TABLE Groupe( 
  	id_groupe NUMBER(20), 
  	nom_groupe VARCHAR2(25), 
	CONSTRAINT pk3 PRIMARY KEY (id_groupe));
	
	CREATE TABLE Membre ( 
	id_groupe NUMBER(20), 
    id_personne NUMBER(20), 
    CONSTRAINT pk4 PRIMARY KEY (id_groupe,id_personne), 
	CONSTRAINT fk3 FOREIGN KEY (id_groupe) REFERENCES Groupe(id_groupe), 
    CONSTRAINT fk4 FOREIGN KEY (id_personne) REFERENCES Personne(id_personne));
    
---------

--creation personnes 
INSERT INTO PERSONNE VALUES (1,'Annie',19);
INSERT INTO PERSONNE VALUES (2,'Alba',20);
INSERT INTO PERSONNE VALUES (3,'George',21);
INSERT INTO PERSONNE VALUES (4,'Samantha',20);
INSERT INTO PERSONNE VALUES (5,'Baldwine',19);
INSERT INTO PERSONNE VALUES (6,'Alfred',17);

-- creation groupes
INSERT INTO GROUPE VALUES (1,'Surf');
INSERT INTO GROUPE VALUES (2,'Yoga');
INSERT INTO GROUPE VALUES (3,'Voyage');
INSERT INTO GROUPE VALUES (4,'Musique');
INSERT INTO GROUPE VALUES (5,'Dance');
INSERT INTO GROUPE VALUES (6,'Jazz');

-- creation ami
INSERT INTO AMI VALUES (1,2);
INSERT INTO AMI VALUES (3,4);
INSERT INTO AMI VALUES (5,4);
INSERT INTO AMI VALUES (5,6);

-- creation membre
INSERT INTO MEMBRE VALUES (1,1);
INSERT INTO MEMBRE VALUES (2,2);
INSERT INTO MEMBRE VALUES (3,2);
INSERT INTO MEMBRE VALUES (6,5);
INSERT INTO MEMBRE VALUES (6,6);
INSERT INTO MEMBRE VALUES (5,4);

-- changement de l'age de george 
UPDATE PERSONNE
SET age = 25 
WHERE nom_personne = 'George';

-- ajout de 1 an à tout le monde
UPDATE PERSONNE 
SET age = age + 1;

-- supression de samantha et geaorge
DELETE MEMBRE
WHERE id_personne = 3 OR id_personne = 4;

DELETE AMI 
WHERE id_personne1 = 3 OR id_personne2 = 3 OR id_personne1 = 4 OR id_personne2 = 4;

DELETE PERSONNE 
WHERE nom_personne = 'George' OR nom_personne = 'Samantha';

-- print table personne
SELECT * 
FROM PERSONNE;
-- supressions à l'envert
DROP TABLE MEMBRE;
DROP TABLE GROUPE;
DROP TABLE AMI;
DROP TABLE PERSONNE;
