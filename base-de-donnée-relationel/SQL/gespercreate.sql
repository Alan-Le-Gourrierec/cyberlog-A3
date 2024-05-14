DROP TABLE salaries CASCADE CONSTRAINTS;
DROP TABLE typearret CASCADE CONSTRAINTS;
DROP TABLE service CASCADE CONSTRAINTS;
DROP TABLE arrettravail CASCADE CONSTRAINTS;
DROP TABLE formation CASCADE CONSTRAINTS;
DROP TABLE suivre CASCADE CONSTRAINTS;
DROP TABLE coefficient CASCADE CONSTRAINTS;
DROP TABLE grille CASCADE CONSTRAINTS;
DROP TABLE categorie CASCADE CONSTRAINTS;

CREATE TABLE categorie(
   codecateg 	NUMBER(2),
   designcateg 	VARCHAR2(30),

   CONSTRAINT pk_categorie 	PRIMARY KEY (codecateg)
);
INSERT INTO categorie VALUES (1,  'Employé');
INSERT INTO categorie VALUES (2,  'Employé');
INSERT INTO categorie VALUES (3,  'Ouvrier');
INSERT INTO categorie VALUES (4,  'Etam');



CREATE TABLE coefficient(
   codecoeff NUMBER(4),

   CONSTRAINT pk_coefficient 	PRIMARY KEY (codecoeff)
);
INSERT INTO coefficient VALUES (100);
INSERT INTO coefficient VALUES (150);
INSERT INTO coefficient VALUES (200);
INSERT INTO coefficient VALUES (250);
INSERT INTO coefficient VALUES (300);
INSERT INTO coefficient VALUES (350);
INSERT INTO coefficient VALUES (400);
INSERT INTO coefficient VALUES (450);
INSERT INTO coefficient VALUES (500);



CREATE TABLE grille(
   codecateg 	NUMBER(2),
   codecoeff 	NUMBER(4),
   salaire 	NUMBER(5),

   CONSTRAINT pk_grille 	PRIMARY KEY (codecateg,codecoeff),

   CONSTRAINT fk1_grille 	FOREIGN KEY (codecateg)	  REFERENCES categorie(codecateg),
   CONSTRAINT fk2_grille 	FOREIGN KEY (codecoeff)   REFERENCES coefficient(codecoeff)
);
INSERT INTO grille VALUES (1,  400,  5500);
INSERT INTO grille VALUES (1,  500,  6500);
INSERT INTO grille VALUES (2,  300,  4000);
INSERT INTO grille VALUES (2,  400,  4500);
INSERT INTO grille VALUES (3,  200,  2500);
INSERT INTO grille VALUES (3,  250,  3500);
INSERT INTO grille VALUES (4,  150,  1500);
INSERT INTO grille VALUES (4,  200,  2000);
INSERT INTO grille VALUES (4,  350,  2500);
INSERT INTO grille VALUES (4,  400,  3000);


CREATE TABLE salaries(
   matricule 	NUMBER(2),
   nom 		VARCHAR2(20),
   prenom 	VARCHAR2(20),
   adresse 	VARCHAR2(40),
   noss 	VARCHAR(20),
   datenais 	DATE,
   anciennete 	NUMBER(2),
   contrat 	VARCHAR2(10),
   creditconge 	NUMBER(3),
   rythme 	VARCHAR2(20),
   codecateg 	NUMBER(2),
   codecoeff 	NUMBER(4),
   noserv 	NUMBER(2),
   
   CONSTRAINT pk_salaries 	PRIMARY KEY (matricule), 

   CONSTRAINT fk1_salaries 	FOREIGN KEY (codecateg) 	REFERENCES categorie(codecateg),  
   CONSTRAINT fk2_salaries 	FOREIGN KEY (codecoeff) 	REFERENCES coefficient(codecoeff)  
);
INSERT INTO salaries VALUES (1,	'Dibou',      'Olivier',   'St Pierre',		'1700464689341', to_date('1990-04-28','YYYY-MM-DD'), 11, NULL,  15, '2.8',    1, 200, 1);
INSERT INTO salaries VALUES (2,	'Bliet',      'Véronique', 'Nantes',		'2720228102852', to_date('1992-02-22','YYYY-MM-DD'), 6,  NULL,  40, '3.8',    1, 400, 3);
INSERT INTO salaries VALUES (3,	'Esnault',    'Jean-Marc', 'Rennes',		'1711035200121', to_date('1991-10-13','YYYY-MM-DD'), 2,  'CDD', 21, 'Normal', 2, 300, 5);
INSERT INTO salaries VALUES (4,	'Derouet',    'Sandrine',  'Saint-Germain',	'2720949210320', to_date('1992-09-01','YYYY-MM-DD'), 1,  'CDI', 10, 'Normal', 4, 400, 1);
INSERT INTO salaries VALUES (5,	'Le Gall',    'Franck',    'Ploumagoar',	'1711022023045', to_date('1991-10-07','YYYY-MM-DD'), 2,  'CDD', 40, '2.8',    3, 200, 2);
INSERT INTO salaries VALUES (6,	'Tual',       'Sophie',    'Rennes',		'2711022140152', to_date('1991-10-22','YYYY-MM-DD'), 1,  'CDI', 23, 'Normal', 4, 350, 4);
INSERT INTO salaries VALUES (7,	'Rams',       'Karine',    'Rennes',		'2730629320210', to_date('1993-06-11','YYYY-MM-DD'), 5,  'CDI', 10, 'Normal', 1, 400, 2);
INSERT INTO salaries VALUES (8,	'Pilet',      'Catherine', 'Rennes',		'2721114020035', to_date('1992-11-20','YYYY-MM-DD'), 5,  'CDI', 2,  '2.8',    2, 300, 4);
INSERT INTO salaries VALUES (9,	'Menard',     'Marie',     'Rennes',		'2730522400200', to_date('1993-05-10','YYYY-MM-DD'), 2,  'CDD', 12, '2.8',    2, 300, 3);
INSERT INTO salaries VALUES (10,'Vuillermoz', 'Claire',    'Betton',		'2641035123452', to_date('1984-10-22','YYYY-MM-DD'), 15, 'CDI', 23, 'Normal', 1, 400, 1);


CREATE TABLE service(
   noserv 		NUMBER(2),
   nomservice 		VARCHAR2(30),
   objectifs 		VARCHAR2(50),
   matriculeresp 	NUMBER(2),

   CONSTRAINT pk_service 	PRIMARY KEY (noserv),

   CONSTRAINT fk1_service 	FOREIGN KEY (matriculeresp) 	REFERENCES salaries(matricule)
);
INSERT INTO service VALUES (1,  'Personnel',     NULL,  1);
INSERT INTO service VALUES (2,  'Informatique',  NULL,  5);
INSERT INTO service VALUES (3,  'Comptabilité',  NULL,  2);
INSERT INTO service VALUES (4,  'Commercial',    NULL,  6);
INSERT INTO service VALUES (5,  'Technique',     NULL,  3);

ALTER TABLE salaries ADD CONSTRAINT fk3_salaries FOREIGN KEY (noserv) REFERENCES service(noserv);



CREATE TABLE typearret(
   codetypearr 	NUMBER(2),
   designarret 	VARCHAR2(30),

   CONSTRAINT pk_typearret 	PRIMARY KEY (codetypearr)
);
INSERT INTO typearret VALUES (1, 'Maladie');
INSERT INTO typearret VALUES (2, 'Accident');
INSERT INTO typearret VALUES (3, 'Thérapeutique');



CREATE TABLE arrettravail(
   noarret 		NUMBER(3),
   datedeb 		DATE,
   datefin 		DATE,
   codetypearr 		NUMBER(2),
   matricule 		NUMBER(2),

   CONSTRAINT pk_arrettravail 	PRIMARY KEY (noarret),

   CONSTRAINT fk1_arrettravail 	FOREIGN KEY (matricule)	  REFERENCES salaries(matricule),
   CONSTRAINT fk2_arrettravail 	FOREIGN KEY (codetypearr) REFERENCES typearret(codetypearr)
);
INSERT INTO arrettravail VALUES (5,  to_date('2016-10-17','YYYY-MM-DD'),  to_date('2016-11-18','YYYY-MM-DD'),  1,  3);
INSERT INTO arrettravail VALUES (6,  to_date('2016-11-20','YYYY-MM-DD'),  NULL,                                2,  3);
INSERT INTO arrettravail VALUES (7,  to_date('2016-12-12','YYYY-MM-DD'),  to_date('2016-12-15','YYYY-MM-DD'),  1,  4);
INSERT INTO arrettravail VALUES (8,  to_date('2017-01-03','YYYY-MM-DD'),  to_date('2017-01-10','YYYY-MM-DD'),  2,  6);
INSERT INTO arrettravail VALUES (9,  to_date('2017-02-02','YYYY-MM-DD'),  NULL,                                3,  4);
INSERT INTO arrettravail VALUES (10, to_date('2017-03-03','YYYY-MM-DD'),  to_date('2017-03-07','YYYY-MM-DD'),  2,  9);
INSERT INTO arrettravail VALUES (11, to_date('2017-03-03','YYYY-MM-DD'),  to_date('2017-04-01','YYYY-MM-DD'),  1,  7);
INSERT INTO arrettravail VALUES (12, to_date('2017-03-05','YYYY-MM-DD'),  to_date('2017-04-12','YYYY-MM-DD'),  2,  5);
INSERT INTO arrettravail VALUES (13, to_date('2017-04-05','YYYY-MM-DD'),  to_date('2017-04-15','YYYY-MM-DD'),  3,  2);
INSERT INTO arrettravail VALUES (14, to_date('2017-04-05','YYYY-MM-DD'),  to_date('2017-04-20','YYYY-MM-DD'),  2,  5);
INSERT INTO arrettravail VALUES (15, to_date('2017-04-06','YYYY-MM-DD'),  to_date('2017-04-10','YYYY-MM-DD'),  3,  8);


CREATE TABLE formation(
   codeform 	NUMBER(2),
   datedeb 	DATE,
   datefin 	DATE,
   type 	VARCHAR2(20),

   CONSTRAINT pk_formation 	PRIMARY KEY (codeform)
);
INSERT INTO formation VALUES (1,  to_date('2016-04-17','YYYY-MM-DD'),  to_date('2016-04-19','YYYY-MM-DD'),  'Gym');
INSERT INTO formation VALUES (2,  to_date('2016-11-24','YYYY-MM-DD'),  to_date('2016-11-30','YYYY-MM-DD'),  'Raft');
INSERT INTO formation VALUES (3,  to_date('2016-05-20','YYYY-MM-DD'),  to_date('2016-05-30','YYYY-MM-DD'),  'Parapent');
INSERT INTO formation VALUES (4,  to_date('2016-06-01','YYYY-MM-DD'),  to_date('2016-06-05','YYYY-MM-DD'),  'Boxe');


CREATE TABLE suivre(
   matricule 	NUMBER(2),
   codeform 	NUMBER(2),

   CONSTRAINT pk_suivre 	PRIMARY KEY (matricule,codeform),

   CONSTRAINT fk1_suivre 	FOREIGN KEY (matricule)	  REFERENCES salaries(matricule),
   CONSTRAINT fk2_suivre 	FOREIGN KEY (codeform) 	  REFERENCES formation(codeform)
);
INSERT INTO suivre VALUES (1,  1);
INSERT INTO suivre VALUES (1,  2);
INSERT INTO suivre VALUES (3,  2);
INSERT INTO suivre VALUES (3,  3);
INSERT INTO suivre VALUES (3,  4);
INSERT INTO suivre VALUES (5,  2);
INSERT INTO suivre VALUES (6,  2);
INSERT INTO suivre VALUES (6,  3);
INSERT INTO suivre VALUES (8,  1);
INSERT INTO suivre VALUES (9,  1);
INSERT INTO suivre VALUES (10, 4);

------ TD 1 ------

SELECT *
FROM formation;

SELECT nomservice
FROM service;

SELECT nom, prenom, noserv
FROM salaries;

SELECT nom, prenom
FROM salaries 
WHERE noserv = 2;

SELECT nom, prenom
FROM salaries 
WHERE adresse = 'Rennes' AND rythme = 'Normal';

SELECT nom, prenom
FROM salaries 
WHERE adresse <> 'Rennes' OR rythme <> 'Normal';

SELECT nom, prenom
FROM salaries 
WHERE noss LIKE '2%';

SELECT nom, prenom
FROM salaries 
WHERE adresse IN('Rennes','Betton') AND contrat <> 'CDD';

SELECT DISTINCT contrat
FROM salaries
WHERE contrat IS NOT NULL;

SELECT matricule 
FROM salaries 
WHERE anciennete BETWEEN 5 AND 10;

SELECT nom 
FROM salaries
ORDER BY nom ASC;

------ TD 2 ------

-- EXERCIE 1
SELECT  nom, nomservice
FROM salaries, service
WHERE (salaries.noserv = service.noserv);

SELECT matricule, type
FROM formation, suivre
WHERE (suivre.codeform = formation.codeform);

SELECT nom, prenom, codetypearr, datedeb, datefin
FROM salaries, arrettravail
WHERE salaries.matricule = arrettravail.matricule;

SELECT nom, type
FROM salaries, formation, suivre
WHERE salaries.matricule = suivre.matricule AND formation.codeform = suivre.codeform;

SELECT nom
FROM salaries, arrettravail
WHERE salaries.matricule = arrettravail.matricule AND arrettravail.datefin IS NULL;

SELECT nom, salaire
FROM salaries, grille
WHERE salaries.codecateg = grille.codecateg AND salaries.codecoeff = grille.codecoeff;

SELECT DISTINCT nom
FROM salaries, typearret, arrettravail
WHERE LOWER(salaries.contrat) = 'cdd'
    AND typearret.codetypearr = arrettravail.codetypearr 
    AND salaries.matricule = arrettravail.matricule;
    
SELECT DISTINCT nom
FROM salaries, formation, suivre
WHERE salaries.anciennete > 5
    AND suivre.matricule = salaries.matricule 
    AND suivre.codeform = formation.codeform;
    
-- EXERCICE 2

SELECT s1.nom, s2.nom
FROM salaries s1, salaries s2
WHERE s1.noserv = s2.noserv
    AND s2.noserv = 2 
    AND s1.nom <> s2.nom;
    
SELECT nom, prenom
FROM salaries, service
WHERE salaries.matricule <> service.matriculeresp
    AND salaries.noserv = service.noserv;
    
--EXERCICE 3

SELECT matricule
FROM salaries
MINUS
SELECT matriculeresp
FROM service;

SELECT nom, adresse
FROM salaries
MINUS
SELECT nom, adresse
    FROM salaries, arrettravail
    WHERE salaries.matricule = arrettravail.matricule;
    
SELECT nom --faux il y en à que 4
FROM salaries
INTERSECT
SELECT nom
FROM salaries, service
WHERE salaries.noserv = service.noserv
	AND salaries.noserv BETWEEN 2 AND 3;

SELECT DISTINCT nom, prenom --faux il y en a que 3
FROM salaries
MINUS
SELECT nom, prenom
FROM salaries, suivre
WHERE salaries.matricule = suivre.matricule;

SELECT type
FROM formation, suivre, salaries
WHERE formation.codeform = suivre.codeform 
	AND salaries.matricule = suivre.matricule
	AND salaries.nom = 'Le Gall';
INTERSECT
SELECT type
FROM formation, suivre, salaries
WHERE formation.codeform = suivre.codeform 
	AND salaries.matricule = suivre.matricule
	AND salaries.nom = 'Tual';

--EXERCICE4

SELECT COUNT(nom) AS TAmount
FROM salaries;

SELECT AVG(anciennete) AS TVieux
FROM salaries;

SELECT MIN(anciennete) AS MINanceinnete, MAX(anciennete) AS MAXanciennete
FROM salaries
WHERE contrat <> 'CDD';

SELECT COUNT(noarret) AS NombreArret
FROM arrettravail
WHERE datedeb > TO_DATE('2017-01-01', 'YYYY-MM-DD');

SELECT SUM(datefin-datedeb) AS LostDays
FROM arrettravail;

------ TD 3 ------

--EXERCICE 1

SELECT noserv,SUM(matricule) AS AmountSalaries
FROM salaries
GROUP BY noserv;

SELECT contrat, AVG(anciennete) AS Ancienneté
FROM salaries
GROUP BY contrat;

SELECT adresse,COUNT(matricule) AS Habitant
FROM salaries
WHERE LOWER(contrat) = 'cdi'
GROUP BY adresse;

SELECT service.nomservice, SUM(salaries.matricule) AS AmountSalaries
FROM service
JOIN salaries ON service.noserv = salaries.noserv
GROUP BY service.noserv, service.nomservice;

SELECT formation.type, COUNT(suivre.matricule) AS Participants
FROM formation
JOIN suivre ON suivre.codeform = formation.codeform
GROUP BY formation.type;

--EXERCICE 2

SELECT nom
FROM salaries
WHERE noserv = (SELECT noserv
    FROM service
    WHERE nomservice = 'Personnel');

SELECT nom, prenom, matricule
FROM salaries
WHERE matricule IN (SELECT matricule
	FROM suivre);
    
SELECT nom, prenom, matricule 
FROM salaries
WHERE matricule IN (SELECT matricule
    FROM suivre,formation
    WHERE suivre.codeform = formation.codeform AND formation.type = 'Raft');

SELECT nom,prenom, matricule
FROM salaries
WHERE anciennete > (SELECT AVG(anciennete) AS test
    FROM salaries);

--EXERCICE 3

SELECT nomservice
FROM service
WHERE noserv IN (SELECT noserv 
	FROM salaries
	GROUP BY noserv
	HAVING COUNT(noserv) > 2);

SELECT type
FROM formation
WHERE codeform IN (SELECT codeform
	FROM suivre
	GROUP BY codeform 
	HAVING COUNT(codeform) > 3);
	
SELECT type
FROM formation
where codeform = (SELECT codeform
    FROM suivre
    GROUP BY codeform
    HAVING COUNT(codeform) >= ALL(SELECT COUNT(codeform) as test
        FROM suivre
        GROUP BY codeform)); 
        
SELECT nom, prenom
FROM salaries
WHERE matricule IN(SELECT matricule
    FROM suivre 
    WHERE codeform IN (SELECT codeform
        FROM formation
        WHERE (datefin-datedeb) > 5));
