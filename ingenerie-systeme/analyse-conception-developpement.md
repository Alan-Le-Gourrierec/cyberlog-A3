
le temps de nuggets : 
- mais pk ?
- AB
- Spécification contre conception
- spécification
- architecture technico fonctionnelle
- conception - comportement existant attendu 
- conception, structuration de code et des données

# Mais pk on fait ca ? 

pour répondre à une demande, vu que on va pas taffer pour le fun et du temps à perdre. 

[MS vs GM](https://archive.framalibre.org/article1886.html)

Quand nous créons un logiciel, nous passons une grande partie de notre temps à fixe les problèmes (72 % pour plus de 3700 entreprises). Deplus 20% des projet sont voué à être des échecs de base avant l’exécution. 

Tout ceci arrive à cause d'une mauvaise gestion dans le but de contre-balancer, il faut une implémentation en top-down afin de pouvoir faire les teste unitaire dans le but de savoir ou se trouve l'erreur. Si pb => nous savons d'ou il vient 

# Analyse du besoin

application, donner l'heure. 
=> scan d'un QR code => donner l'heure 

- contexte : connaître l'heure. 
	- rapide
	- précis
	- affichage : heure/minute/seconde
	- fuseau horaire 

Spécification :
- délai : ~500ms
- distance du scan
- connectivité

paramètres de conception :
- technologie (js,ts, tsx, jsx)
- architecture 
---
Contrat : 
- localisation : tuple(string) 
- date : date  => Date.now()
- afficher-date() : void 
- calcule-date() : date
---
---
QR-code :
- url : str qui redirige vers une page web
- fuseau horaire
---
Préparer un plan de travaille pour traduire au client ce qu'il faut faire dans le but que tout le monde s'entends bien. 

Nous retrouvons ceci dans plusieurs domaines, aussi bien l'agroalimentaire que l'informatique (exemple, la pasteurisation pour traiter les produire. Par exemple, temps sous 120 °C <20s, temperature <70°C pour le pasteuriser. En gros l’équivalent en prog serais de renvoyer une erreur).

Le client va donc faire une EBI qui est une poubelle à idée 

la conception répond  à comment créer l'aplication pour répondre au spécification produit 

la spécification de l'archi décrit le fonctionnement du produit. Dans le but de bien organiser le produit. 

La phase d'analyse est nécéssaire, elle permet de bien poser le problème avant de commencer. Nous allons créer des normes pour que tout le monde puisse parler le même langage et ne pas avoir d’ambiguïté entre tout le monde et:
- pas de complexité 
- pas d’exhaustivité 
- simple 
- facile de compréhension


Jeu de données => mon entité horloge. Nous allons simuler ce que nous devons avoir en réception.

Les teste doivent être réalisé des composant les plus petit au plus grand (et faire un teste globale avant)

tester => pour se faire, nous allons faire un teste unitaire avant l'implémentation. 
donc on va faire : 
- test unitaires => permet de voir si le component ne marche pas
- test d'intégration => 
- test d'IHM
- test de snapchots

l'objectif est de trouver 90% de fiabilité.  Teste TDD (cf sur internet vu que flem d'écrire)




