
un joueur ne peux pas avoir le même id que son adversaire
```ocl
Context Joueur
inv : self.identifiant <> self.adfversaire.identifiant
```

l'age dois être supérieur à 3 (age mini théorique pour jouer) 
```ocl
Context Joueur
inv : self.age > 3 
```

taille porte-avion
```ocl
Context Flotte
inv : self.bateau = "Porte-avion" implies self.taille = 5 and self.case->sum()=5
```

taille croiseur 
```ocl
Context Flotte
inv : self.bateau = "Croiseur" implies self.taille = 4 and self.case->sum()=4
```

taille contre-torpilleur
```ocl
Cotext Flotte
inv : self.bateau = "Contre-torpilleur" implies self.taille = 3 and self.case->sum()=3
```

taille torpilleur 
```ocl
Context Flotte
inv : self.bateau = "Torpilleur" implies self.taille = 2 and self.case->sum()=2
```

coordonnées comprise entre 1 et t10 (pour x) et 1 et 10 (pour y)
```ocl
Context Case 
	inv : self.positiony->forAll(pos | pos>=1 and pos <= 10) and self.positionx->forAll(pos | pos>=1 and pos<=10)
```

prochain tour à définir
```ocl
Context Carte::prochain-tour():Reel
inv : self.nombre_de_tour + 1
```

quand une case est attaqué, elle passe en touche = TRUE
```ocl
Context Joueur::torpiller(posx:Real,posy:Real):Bool
pre : posx>=1 and pox<=10 and posy<=1 and posy>=10
post : self.grille.case->forAll(p1,p2 | p1 = posx and p2 = posy implies self.touche = True) 
```

Réinitialisation :
```ocl
Context : Grille::reinitialisation():void
inv : self.Case->forAll(self.touche= False) 
	and self.Joueur.Flotte->forAll(self.coule=False)
```

Quantité de bateau : 
```ocl
Contexte Joueur
pre : self.Bateau->sum()=5
inv : self.Bateau->forAll(['porte-avion','croiseur','torpilleur','contre-torpileur']->include(self.Bateau)) and self.Bateau->select(self.bateau = 'contre-torpilleur')->size()=2
```