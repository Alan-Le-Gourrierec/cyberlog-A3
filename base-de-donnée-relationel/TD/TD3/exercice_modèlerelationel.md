# Exercice BD (niveau intermédiraire) 
> Alan, 11 septempbre 2023 

[[exercice2]] [[musee]] [[entite-assossiation.pdf]]
Auteur (nom,prénom,pseudonyme) 

**CP** : (nom,prénom) | **CE** : --

Livre.prix_litéraire (Livre.ISBN, pl.nom, pl.année) 

**CP** : (livre.ISBN , pl.nom, pl.année) | **CE** : (Livre.ISBN)

---
Livre (ISBN,titre)

**CP** : (ISBN) | **CE** : --

---

Librarie (nom, adresse.rue, adresse.code_postal, adresse.ville)

**CP** : (nom, adresse.rue, adresse.code_postal, adresse.ville) | **CE** : -- 

---

Édition (Livre.ISBN, PrixVente, numéro, nbr_exemplaires, année)

**CP** : (Livre.ISBN, numéro) | **CE** : (Livre.ISBN)

---

Écrire (Livre.ISBN, Auteur.nom, Auteur.prénom, droits-auteurs)

**CP** : (Livre.ISBN, Auteur.nom, Auteur.prénom) | **CE** :(Livre.ISBN, Auteur.nom, Auteur.prénom)

--- 

Commander(Livre.iSBN, adresse.rue, adresse.code_postal, adresse.ville, quantité, date.jour, date.mois, date.année) 

**CP** : (Livre.ISBN, adresse.rue, adresse.code_postal, adresse.ville) |
**CE** : (Livre.ISBN, adresse.rue, adresse.code_postal, adresse.ville)

# type entité faible 

* Nom : éditeur
* Sémantique : nom de la maison d'édition du livre
* Type : type entité _faible dépendant du TE **"fort"** Livre et lié par le TA faible paru_
* Attributs :
    * Attribut 1:
        * Nom : nombre d'exemplaire
        * Sémantique : nombre d'éxemplaires créé pour cette édition du livre en question
        * Cardinalité : 1:1
        * Domaine : int
    * Attribut 2 : 
        * Nom : numéro 
        * Sémantique : le numéro de l'édition et/ou réédition du livre en question 
        * Cardinalité : 1:1
        * Domaine : int
    * Attribut 3 : 
        * Nom : prix 
        * Sémantique : prix fixé par la maison d'édition pour cette édition de ce livre précis 
        * Cardinalité : 1:1
        * Domaine : int
    * Attribut 4 :
        * Nom : date de parution
        * Sémantique : date ou le livre est sorti 
        * Sous-attribut :
            * Sous-attribut 1:
                * Nom : jour 
                * Sémantique : jour de parution 
                * Cardinalité : 1:1
                * Domaine : int
            * Sous-attribut 2 :
                * Nom : mois
                * Sémantique : mois de parution
                * Cardinalité : 1:1
                * Domaine : int
            * Sous-attribut 3 : 
                * Nom : année 
                * Sémantique : année de parution
                * Cardinalité : 1:1
                * Domaine : int
        * Cardinalité : 1:1
* Cardinalité : 1:1
* Identifiant : **Livre.ISBN**, numéro
* CI : 
    * Dois être une maison d'édition conforme à la liste des maison d'édition existante
    * la date doit être conforme 

# Type action 
* Nom : Éditer
* Sémantique : édition du livre par un éditeur
* TE participant et cardinalié :
    * Éditer : 1:1 (TE faible)
    * Livre : 1:1 (TE fort)
* Type : type action faible 
* Identifiant : **Livre.ISBN**, **Éditeur.numéro** 

