[[Langage-UML-pour-modelisation-statique]]
son existance est du à l’insuffisance de la représentation des contraintes :
langage formel sans ambiguité, langage déclaratif, quoi mais pas comment. 

3 types de contraintes et non le corp de la méthode : 
- expressions booléen 
- contraintes invariantes : toujours respecté => respecté/vérifier **précondition** =>avant la méthode et **postcondition** => condition après la méthode 

post condition :
=> result : représente le résultat
=> @pre : la valaur de l'atribut avant l'exec de la méthode 
- mon_attribut@pré (on peu aussi utiliser post)

```ocl
context Compte::debiter(montant:int) : integer
pre:montant>0
post: solde = solde@pre - montant
```

```ocl
context Compte::getSolve():int
post: result = solde
```
Toute contraintes commences par :
- **context** *nomdelamdethode* **:** 
- **body** requet pour représenter le corps de la méthode (dois être une simple requête)
- **init** : initialisation 
- **derive** : expression qui représentant la règle de dérivation (on peu obtenir sa valeur grâce à des calculs)

Ceci marche un peu comme des bdd, on va utiliser le nom de rôle, si il n'y à pas de rôle => on utilise le nom de la classe en minuscule. 
Utilisation de Set(*nom de la classe*) 
si on utilise ordered => Setordered(*nom de la classe*)

---


```ocl
context Personne
inv : self.compte.solde -> sum() <=
```

4 types de collection :
- Set : ensemble au sens mathématique, pas de doublons, sans ordre
- OrderedSet : Set mais ordonné
- Bag : donne la possibilité avoir des doublons
- Sequence : Bag ordonnée

> Depuis OCL 2, nous pouvons appliquer une sytaxe d'utilisation, comme par exemple : size():int, isEmpty():boot, notEmpty():bool, includes(obj):bool, excludes(obj):bool, including(obj):add objet, excluding(obj):¬including, includeAll(ensemble):bool, excludeAll(ensemble) : bool.

	cf page 33

On peu faire des opération sur des ensembles. 
- select : retourne les éléments qui respect les paramètres
- reject : rejet des élément qui ne respect pas les paramètres
- collect : applique une fonction comme map en python (ou en OCAML DE SES GRANDS MORTS) => same size 

3 facons d'éfectuer des opérations sur les éléments :
- compte->select(c : Compte| c.solde > 1000)
- compte->select( c | c.solde > 1000)
- compte->select(solde > 1000)

c: Compte, pose une variable c de typer compte 

- select (contrainte) => retourne les éléments répondant à la condition
- reject (contrainte) => retourne les éléments ne répondant pas à cette condition 
- collect (expression) => retourne les éléments des colones sélectionnés 
- exist (contrainte) => bool si il existe un élément qui répond à la contrainte 
- forAll (contrainte) => bool si tout les **éléments** respecte la contrainte

```ocl
collection->iterate(element : Type;
accumulateur : Type = expression-init |
expression-avec-accumulateur-et-element)
```
	cf page 44


syntax
- if exp1 then exp2 else exp3 endif
- ou => exp1 implies exp2
```ocl
context Personne
let argent = self.compte.solde->sum() in
self.age >= 18 implies argent > 0
```

let est une variable local

```ocl
context Personne
def: argent : Integer = self.compte.solde->sum()
inv: self.age >= 18 implies argent > 0
```

def et une variable global. 

```ocl 
context Personne
inv: Personne.allInstances()->forAll(p1, p2 |
p1 <> p2 implies p1.nom <> p2.nom)
```
allinstance() permet de sélectionner tout les occurrences, p1 et p2 son deux personne distinct. 

![[Pasted image 20231116083611.png]]

```ocl
context Company
inv: self.manager.IsUneemployed = false and
	 self.manager.age > 40 and
	 self.employer -> notEmpty()

context Company::hireEmployee(p: Personne)
pre: self.employee->exclude(p)
post:self.employee->include(p)
```

```ocl
context Personne::income(): Real
post : 
	 if self.age <18 then 
		 result = (self.parent.job.salariy()->sum*0.01)
	 else 
		 result = self.job.salay->sum()
	 endif
```
