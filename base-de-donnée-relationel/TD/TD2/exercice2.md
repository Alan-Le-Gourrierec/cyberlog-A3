# Type Entité :

[[entite-assossiation.pdf]]
[[exercice2]]
## type entité 1 :
* Nom : Client
* Sémantique : information relevant du client 
* Type : type entité fort
* Sous-attributs : 
    * Sous-attribut 1 :
        * Nom : num
        * Sémantique : numéro untique associé à un client 
        * Cardinalité : 1:1
        * Domaine : int
    * Sous-attribut 2 : 
        * Nom : nom 
        * Sémantique : nom du client concerné 
        * Cardinalité : 1:1
        * Domaine : string
    * Sous-attribut 3 :
        * Nom : prénoms 
        * Sémantique : liste des prénoms du client concerné
        * Cardinalité : 1:n
        * Domaine : string 
    * Sous-attribut 4 :
        * Nom : caution
        * Sémantique : caution donné à l'inscription permétant un certain nombres d'emprint 
        * Cardinalité : 1:1
        * Domaine : int
    * Sous-attribut 5 :
        * Nom : adresse 
        * Sémantique : adresse du client 
        * Sous-attributs :
            * Sous-attribut 1 :
                * Nom : rue 
                * Sémantique : rue ou habite le client 
                * Cardinalité : 1:1
                * Domaine : string
            * Sous-attribut 2 : 
                * Nom : ville 
                * Sémantique : ville ou habite le client 
                * Cardinalité : 1:1
                * Domaine : sting 
            * Sous-attribut 3 :  
                * Nom : code postal
                * Sémantique : code postale de la ville du client 
                * Cardinalité : 1:1
                * Domaine : int
    * Cardinalité : 0:n
    * Identifiant : num
    * CI : 
        * code postal conforme   
        * code postal corespondant à la ville 

---
## Type entité 2 : 
* Nom : DVD
* Sémantique : un DVD
* Type : type entité fort 
* Attribut :
    * Attribut 1 :
        * Nom : numéro
        * Sémantique : numéro unique pour identifier un DVD
        * Cardinalité : 1:1
        * Domaine : int
    * Attribut 2 :
        * Nom : état 
        * Sémantique : état du DVD 
        * Cardinalité : 1:1
        * Domaine : char (lettre représentant l'état du livre)
    * Attribut 3 :
        * Nom : magasin
        * Sémantique : numéro du magasin 
        * Cardinalité : 1:1
        * Domaine : int 
    * Attribut 4 :
        * Nom : date d'achat 
        * Sémantique : date d'achat du DVD
        * Type : attribut multivalué
            * Sous-attribut 1 : 
                * Nom : jour d'achat 
                * Sémantique : jour d'achat du livre 
                * Cardinalité : 1:1
                * Domaine : int
            * Sous-attribut 2 :
                * Nom : mois d'achat 
                * Sémantique : mois d'achat du livre 
                * Cardinalité : 1:1
                * Domaine : int
            * Sous-attribut 3 :
                * Nom : année d'achat 
                * Sémantique : année d'achat 
                * Cardinalité : 1:1
                * Domaine : int
* Cardinalité : 0:n
* Identifiant : numéro
* CI : 
    * une date conforme 
    * un numéro de magasin compris entre 0 et 9 

---
## type entité 3 : 
* Nom : Film
* Sémantique : information relatives au film 
* Type : type entité faible 
* Attributs : 
    * Attribut 1:
        * Nom : acteurs 
        * Sémantique : liste des acteurs principaux du film
        * Cardinalité : 0:n (il n'y à pas forcément d'acteur dans les films d'animation)
        * Domaine : string
    * Attribut 2 :
        * Nom : réalisateur
        * Sémantique : nom du réalisteur du film
        * Cardinalité : 1:1
        * Domaine : string
    * Attribut 3 : 
        * Nom : durée 
        * Sémantique : durée du film
        * Cardinalité : 1:1
        * Domaine : int (temps en seconde)
    * Attribut 4 :
        * Nom : genre
        * Sémantique : information concernant le genre et le nom du film
        * Sous-attributs :
            * Sous-attribut 1 :
                * Nom : titre 
                * Sémantique : titre du film
                * Cardinalité : 1:1
                * Domaine : string 
            * Sous-attribut 2 :
                * Nom : type 
                * Sémantique : type de film pour savoir à quelle publique celui-ci s'adresse
                * Cardinalité : 1:n (un film à souvent plusieurs genre)
                * Domaine : string
* Cardinalité : 1:1
* Identifiant : numéro (prends l'identifiant de précédent)
* CI : 
    * durée du film infèrieur à 22h ([La Flor](https://fr.wikipedia.org/wiki/La_flor) dure 13h34)
    * le nom des acteurs dois être correcte par rapport au film 


---
# Type Attribut : 

* Nom : Emprint 
* Sémantique : emprint d'un DVD par un client 
* Type : type attribut fort 
* Attribut :
    * Attribut 1 :
        * Nom : date d'emrpint 
        * Sémantique : date ou le client à emprinté le DVD
        * Sous-Attributs :
            * Sous-attribut 1 : 
                * Nom : jour d'emprint 
                * Sémantique : jour d'emprint du livre 
                * Cardinalité : 1:1
                * Domaine : int
            * Sous-attribut 2 :
                * Nom : mois d'emprint 
                * Sémantique : mois d'emprint du livre 
                * Cardinalité : 1:1
                * Domaine : int
            * Sous-attribut 3 :
                * Nom : année d'emprint 
                * Sémantique : année d'emprint 
                * Cardinalité : 1:1
                * Domaine : int
        * Cardinalité : 1:1
    * Attribut 2 :
        * Nom : date de retour
        * Sémantique : date ou le DVD à été ramené par el client 
        * Sous-attributs:
           * Sous-attribut 1 : 
                * Nom : jour de retour 
                * Sémantique : jour de retour du livre 
                * Cardinalité : 1:1
                * Domaine : int
            * Sous-attribut 2 :
                * Nom : mois de retour 
                * Sémantique : mois de retour du livre 
                * Cardinalité : 1:1
                * Domaine : int
            * Sous-attribut 3 :
                * Nom : année de retour 
                * Sémantique : année de retour 
                * Cardinalité : 1:1
                * Domaine : int
        * Cardinalité : 0:1
* Identifiant : Client.num, DVD.numéro (le identifiant des précédants) et Date d'emprint
* CI : 
    * Le client peu emprinter entre 1 et 6 livres  
---
## Type Attribut 2 :
* Nom : contient 
* Sémantique : ce que contiens le DVD 
* Identifiant : numéro (identifiant de film)

