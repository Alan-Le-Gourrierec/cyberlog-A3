- la carte est carré (10x10)
- les bateau sont avec un x ou un y constant 
- les bateau sont sur la carte
- on attaque des bateau sur la carte 
- le joueur ne peux pas avoir un age négatif 
- le nombre de bateau est constant = 5
- la taille des bateau
	- 5 porte-avions
	- 4 croiseur
	- 3 contre- torpilleur
	- 2 torpilleur
- une case ne peux pas changé d'état une fois touché 

```ocl
context Joueur
inv : self.age > 0
```

```ocl
context 
```