
## Exerecice 1

#### question 1

```ocl
context Job::salary(): Real
init: 1000
```

#### question 2

```ocl
context Company
inv:slef.manager.age > 40
```

#### question 3

```ocl
Context Personne
derive self.age = Date::now() - self.birthDate
```

#### question 4

```ocl
context Company::turnOver()>1000000: Real
inv: elf.employer->size() > 10
```

#### question 5

```ocl
context Personne
inv: self.job->forAll(c | c.startDate < self.birthdate)
```

#### question 6

```ocl 
context Mariage
inv: self.wife.gender = #femmel and self.husband.gender = #homme
```

#### question 7
```ocl
contexte Personne
derive self.isMarried implies self.age > 18
```

#### question 8

```ocl
context Job
derive : self.employee.isMaried implies
	self.startDate <> self.employee.maried.date
```

#### question 9

```ocl
context Personne
inv: self.employeur->size() < 3
```

#### question 10

```ocl
context Company 
inv: self.emplyee->forall(age>=18)
```

#### question 11

```ocl
context Company
derive : self.employee->size()+1
```

#### question 12

```ocl
context Personne
pre : age > 18
body: if self.isUnemployed then 0 else self.salary->sum() endif
```
#### question 13

```ocl
context Company
inv : self.employee->exists(age>50)
```

#### question 14

```ocl
contexte Personne
inv : self.Parents->forAll(p1,p2| p1 <> p2 implies P1.gender <> P2.gender)
```

#### question 15

```ocl
Context Personne 
inv : self.child->notEmpty() implies self.child->forAll(p.parent| p.parent->includer(self))
inv : self.parent->forAll(p.parent| p.child->include(self))
```

## Exercice 2

#### question 1
<p> Un hôtel ne contient jamais d'étage numéro 13 </p>
```ocl
context chambre
inv : self.etage <> 13
context Salledebain
inv : self.etage <> 13
```

#### question 2

<p>Le nombre de personnes par chambre doit être inférieur ou égal au nombre de lits dans la
chambre louée. Les enfants (accompagnés) de moins de 4 ans ne comptent pas dans cette
règle de calcul (à hauteur d'un enfant de moins de 4 ans maximum par chambre)</p>

```ocl
context Chambre
inv : slef.client->size<=nombreDeLit or (self.client->size()=nombreDeLit+1 
and self.client->existe(P.personne|p.age<4))
```

#### question 3
<p> L'étage de chaque chambre est compris entre le premier et le dernier étage de l'hôte </p>
```ocl 
context Chambre
inv : self.etage <= self.hotel.etageMax and self.etage >= self.hotel.etageMin
```

#### question 4

<p>Chaque étage possède au moins une chambre (sauf le 13 qui n'existe pas, bien entendu...) </p>
```ocl
context Hotel
inv : sequence{etageMin ... etageMax}-> forAll(i:Integer)i<>13 implies self.chambre->existe(etage=i))
```

#### question 5

<p> On ne peut repeindre une chambre que si elle n'est pas louée. Une fois repeinte, une
chambre coûte 10% de plus </p>
```ocl
context Chambre
pre : self.client-> isEmpty()
Post: Prix=prix@pre*1.1
```

#### question 6

<p> Une salle de bain privative ne peut être utilisée que par des personnes qui louent la chambre
contenant la salle de bains et une salle de bains sur le palier ne peut être utilisée que par les
clients qui logent sur le même palier</p>

```ocl
context Salledebain
pre: if self.chambre->notEmpty them self.chambre.client->includes(p)
	else p.chambre.etage = self.etage
post: nbUtilisateur = nbUtilisateur@Pre+1
```

#### question 7

<p> Le loyer de l'hôtel (calculerloyer()) est égal à la somme du prix de toutes les chambres
louées </p>
```
context Hotel
post: result = self.chambre-> select(client->notEmpty).prix->sum()
```
