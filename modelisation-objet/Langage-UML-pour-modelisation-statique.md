[[Concepts-fondateurs-objet]]
[[chapitre 2 - diagramme de classe2324.pdf]]

Pour modéliser notre application, nous allons identifier mes divers concepts dans l'application. Nous allons donc modéliser en divers objets avec un différent niveau de détails, nous compléterons le diagramme des classe au fur et à mesure du déroulement du projet (FRANCE DE MERDE AVEC SES PROJETS PARTOUT).

> Pour représenter, on le fait en 3 partie : Son nom | ses attributs | ses méthodes 

### Phase d'analyse 

- niveau simplfié
	- nom only
- niveau intermédiaire 
	- nom de la classe
	- nom des attributs ou (exclusif) de méthodes
- complet
	- nom de la classe
	- nom de attributs
	- nom des méthodes

### Conception

- Attributs 
	- Type
	- valeur par défaut 
	- degré de visibilité
- Méthode
	- nom fonction
	- description des fonctions (l'encapsulation est précisé)

attributs  $\Rightarrow$ souligner les ces pauvres 
attributs $\Rightarrow$ non nécessaires ou peu être obtenu de façons diverses  

type enumération $\Rightarrow$ ensemble fini de valeurs genre le nom des jours dans la semaine.  

## Multiplicité ou cardinalité 

si multiplicité =:
- 1 => lié à un objet 
- 0..1 => zéro ou un
- M..N => entre M ou N
- * => 0 ou plusieurs 
- N => lié à exactement N objet
- 1* => 1 à plusieurs

Les flèches sont bidirectionnels 

## Classe association 

Nous pouvons avoir des "sous-association" dans les tableaux des attributs. En gors on fait des bd déguisé en nous disant que c'est pas le cas 
![[Pasted image 20231109120603.png]]

Ils ont même pris les dépendance de c'est salaud !!!
Nous pouvons aussi faire des liaison avec n mais on évite de dépasser les 3 pour des question de lisibilité.

### Agrégation 

si sémantique comporte contiens ou comportes $\Rightarrow$ agrégation et son ptit nom c'est agrégat 
Pour les distinguer on utilise un losange vide.

### Composition 

représenté par un losange noir 
agrégation forte : Si objet détruit et que tout disparaît => composition 

### Généralisation 

homme et femme (sous classe) -> personnes (super classe) 

- les sous classe héritent des propriété des super classes 
- les classes enfant possèdent les propriété de ses classes parents 

l'héritage est une relation transitive : A ne peux pas hériter de B et B ne peux pas hériter en même temps de A.

## Contrainte sur les association 

- cardinalité 
- \[ordred] => les élément de la colletion sont ordonnée 
- \[xor] =>

> complet : nos cas prènent en compte tout $\Omega$ 
> disjoint : on ne peux appartenir qu'à une classe 

**exemple**

homme femme => personne (disjoint et complet)
etudiant enseignant => personne (incomplet et overlaping)

---
classe abstract => peu pas l'appeler comme je le veux et l'utiliser comme je veux 
(représenté par sois *ma_fonction_débile()* ou par ma_fonction_débile(){abstract})

le diagramme d'objet représente l'ensemble des objets qui existent à un instant $t$ 

on apprends à utiliser star UML

trait entre les objets = liens et non association 