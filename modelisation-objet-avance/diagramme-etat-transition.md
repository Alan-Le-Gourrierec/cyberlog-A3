on le fait que pour les classes avec un comportement complexe ou pour le système entier

~10% des classes dans un système 
pour un amphithéâtre 

Une activité peu être exécuté sois à l'entré sois à la sortie d'un état.
durant un état on peu réagir à un événement lors de sa réception 


état final => fin de cycle de vie de l'objet et il peux rester dans cette état pour tjr 

état de transition => l(objet arrête d’exister) 

il y à 3 transitions :
- entry : entre dans l'état
- do : tant que l'objet reste dans cette état
- exit : quand il quite l'état

un événement peux avoir des paramètres 

auto-transition stay dans le même (en gros comme en iot quand ont fait de thread pour faire clignoter de la merde)

4 façons :
- pas de garde , à la fin de A1 on pas à l'état S2
- si A1 est terminé et la garde g1 est valide on passe à S2
- on passe automatiquement avec un événement completions
- on passe automatiquement avec un événement completions si la garde est valide

call : appel de méthode 
change : si condition vrai => on change sinon on reste
signal : 
after : après la fin d'un état déterminé 

```
when( condition bool) #transition vers un nouvel état si vrai
```

```
after(durée) #transition si un certains temps est passé 
```

auto-transition on sors et entre dans un état. on perds le contexte 
transition interne on conserve le contexte 

le symbole de join est un cercle noir plein et permet de simplifier le truc 
le symbole losange est fork qui permet de faire des trus en parallèle 

la bar permet de lancer des trucs en parallèle.

en gros fork => split de task de 1 à n 
join => join task de n à 1