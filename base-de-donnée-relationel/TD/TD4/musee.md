# Schéma reltionelle 
[[entite-assossiation.pdf]] [[exercice2]]
Oeuvre(n°,titre)
- **CP** : n° (elle est unique pour chaqeu oeuvres)
- **CE** : --

Oeuvre.auteurs(Oeuvre.n°,auteurs)
- **CP** : Oeuvre.n°
- **CE** : Oeuvre.n° ref : n° de la relation Oeuvre

Nos oeuvres(Oeuvre.n°,jour d'aquisition, mois d'aquisition, année d'aquisition)
- **CP** : Oeuvre.n° 
- **CE** : Oeuvre.n° ref : n° de la relation Oeuvre

Oeuvres emprinté(Oeuvre.n°)
- **CP** : Oeuvre.n° 
- **CE** : Oeuvre.n° ref : n° de la relation Oeuvre

Salle(n° salle, sol, éclairage, nom, quantité d'oeuvre)
- **CP** : (n° salle)
- **CE** : --

Prêteur(nom, ville, code postal, rue)
- **CP** : (nom, ville, code postal, rue) 
- **CE** : --

Musée(nom, ville, code postal, rue)
- **CP** : Prêteur.nom,Prêteur.ville, code postal, rue
- **CE** : Prêteur.nom,Prêteur.ville, code postal, rue ref nom, ville, code postal, rue de la relation Prêteur

Particuliés(nom, ville, code postal, rue)
- **CP** : Prêteur.nom,Prêteur.ville, code postal, rue
- **CE** : Prêteur.nom,Prêteur.ville, code postal, rue ref nom, ville, code postal, rue de la relation Prêteur

Assurance(nom,ville, code postal, rue)
- **CP** : 
- **CE** : 