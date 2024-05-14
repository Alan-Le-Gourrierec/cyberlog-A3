[[chapitre 1 - Introduction_2024.pdf]]
modélisation statique 
langage OCL $\Rightarrow$ maîtrise des contraintes

Nous allons utiliser le langage OCL impérative avec USE

---
## Cycle de vie 

divers étapes qui forme le cycle de vie du logiciel :
- expression des besoins 
	- déterminer le fonctionnalités
- Analyse du besoin et le comprendre
- Conception 
	- comment qu'on fait ?
- Implémentation
- Test

représentation simplifié (modélisation) pour un problème réel.

Pour le réaliser :
- un langage (surprenant ^^) $\Rightarrow$ notation claire et sémantique précise

---
## <font color = green> Introduction </font>

ULM, créer en 1997, normalisé par OMG (*Object Managment Group*)  
q
Il y à beaucoup de diagrammes (cf p.17)

L'UML seul n'arrive pas à représenter toutes les contraintes $\Rightarrow$ utilisation de OCL et nous utiliserons starUML

---

## <font color = pink> C'est quoi en gros ? </font>

- objet 
- classe
- héritage
- polymorphisme
- encapsulation

**EN GROS C'EST DU JAVA**

### <font color = pink> objets  </font>

>**objet** : représentation d'un objet du monde réel en utilisant un objet du monde réel

> **abstraction** : simplification de l'objet du au point de vue

"Il y à beaucoup de blabla mais peu de choses intéressantes $\Rightarrow$ en gros faire comme en java de base et regarder comment marche starUML pour la modélisation"

### <font color = pink> Classe </font>

moyen de def des truc de statue commun avec le même comportement 

> classe voiture / compte bancaire  
> objet : voiture_de_paul / voiture_de_bob / compte_de_patrick (faux il est au Bahamas) / compte_de_joseph

On retrouve les classe abstraites de java (suprenant ^^)

### <font color = pink> Héritage </font> 

La surclasse hérite de la super classe en gros c'est les extend de java (on y reviens on y reviens encore, ILS AURONT NOTRE PEAU CES DEV JAVA) 

genre voiture : voiture $\Rightarrow$ voiture_de_course $\Rightarrow$ voiture_de_course_de_prolo 
on peu aussi avoir un héritage multiple 

### <font color = pink> Encapsulation </font>

on masque une partie de l'objet (notion de visibilité) avec les type public/protected/private

### <font color = pink> Polymorphysme </font>

Avoir une même méthode qui possède plusieurs formes en gros on peu redéfinir cette méthode pour chaque sous-classe 