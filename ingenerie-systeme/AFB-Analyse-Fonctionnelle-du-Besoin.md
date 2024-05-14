 +
**Identifier les BP :  [[Module2.pdf]]** 
[[Abreviation.pdf]]
## <font color = pink> Identifier les phases (p.113) </font>
 
 >phase : période durant laquelle l'utilisation du Produit est invariable en raison d'une attente et/ou d'un environnement spécifique
 
ce que dois réaliser un produit à un instant t (**exemple voiture :** route, autoroute, garages)<br>
nous aimons aussi créer des arbres et nous ne cherchons pas à les lister de façons exhaustive, nous cherchons à conditionner les divers phases du produit. On cherche à en avoir le moins possible $\rightarrow$ application multiplicative

> Cycle de vie, ensemble des phase du Produit

*Création de la Table des Phases et de la Matrice des phases(peu être représenter sous forme de table, graphique ou cycle* La phase Conception et Déploient n'ont rien à faire dans cette phases ci (on la retrouve en AOT) la seul qui est utile est la phase p.120 du diapo (la p.119 ne sers à rien)

Bilan de liaison $\rightarrow$ perte de signale au fur et à mesure du signale

--- 
## <font color = pink> Élaborer les Scénarios Produit  (p.122) </font>

> SP : récit hypothétique qui décrit très précisément et chronologiquement les interaction souhaité du Produit avec son environnement.

Ceci servent à valider les scénario opérationnel (ils vérifient les (EA/ET/EN) = PO (Processus d'un Organisme)). Il est représenté par une nième table 

---
## <font color = pink> Identifier les Interacteurs(p.127) </font> 

**/!\\Très important** 
> Intercateur : élément en interaction avec le produit au cours de l'une des Phases ou Sous-Phase de sons Cycle de Vie.

**p.129**

Les intéracteur dérivent directement de SP si ces derniers sont bien fait 

---
## <font color = pink> Analyse des Interacteurs (p.133)</font>
Si ils ne sont pas complet, nous devrons faire des allers-retours si ils ne sont pas bien fait !! $\rightarrow$ il faut donc bien faire les SP dès le départ 

> BP : résulte du manque de Solution pour un Produit et son expression traduit ce que le Produit, être et supporter à un instant donné dans une situation donnée.  
> en gros ça résulte d'un manque suite à la poubelle de l'EBU.

FS (Fonction de Service) $\rightarrow$ "ce qu'il doit faire"
C (Contraintes) $\rightarrow$  "ce qu'il doit être fait" / "ce qu'il dois supporter"

> FS : Action demandée à un Produit (ou réalisé par lui), afin de satifaire une partie du Besoin Utilisateur.

- Une FS est formulé par un verbe à l'infinitif
- Une FS exprime ce que "Le Produit dois faire"
- NE JAMAIS DIRE "LE PRODUIT DOIS FONCTIONER"

> C : Limitation à la liberté de choix des concepteurs lors de la définition des Solutions

- Une C est formulé par un verbe à l'infinitif (être ou suporter)

**p.133**
#### <font color = pink> Flèche rose </font>
quand nous allons de l'intéracteur au produit $\rightarrow$ C :
- "Qu'est ce que le Produit doit SUPPOERTER DE OU ÊTRE  vis-à-vis de l'intéracteur"

Si il ext relier à un autre intéracteur (flèches bleu et rose) :
- "Qu'est ce que me Produit dois SUPPORTER de ou ÊTRE vis-àvis de l'intéracteur A à l’initiative d'un Autre Interacteur"
#### <font color = orange>Flèche orange</font>

- "Qu'est ce que le produit dois faire pour l'interacteur E à sa propre initiative"
#### <font color=yellow> Flèche jaune </font>

- "Qu'est ce que le produit dois faire à partir de l'intéraction B pour l'interacteur D à sa propre initiative/à l'initiative de l'intéracteur D/à l'initiative de l'intéracteur B/autre intéracteurs  ?"
### <font color = green> Flèche verte </font>

- "Qu'est ce que le produit dois faire à partir de l'intéraction B pour l'interacteur D à sa propre initiative/à l'initiative de l'intéracteur D/à l'initiative de l'intéracteur B/autre intéracteurs  ?"

Le Problème est donc, si nous avons pas l'entièreté des intéracteurs, ceci va créer des problèmes, et aussi des les regrouper.  
Ensuite nous devons faire la matrice des interactions **IL FAUT QUE LES INTERACTIONS SOIT DISTINCTES, sinon ça va être long** , il y à beaucoup de cellule qui sont NA (non applicable)

Sûreté $\rightarrow$ ne tue pas les gens

---
## <font color = pink>Raffiner mes FS/C (p.146)</font>

>Raffinement : Consiste à préciser les FS/C obtenu par l'analyse des interactions, en créant de nouvelles et en structurant l'ensemble des FS/C ainsi obtenu.

- il faut limiter le nombre de branches sur les premiers niveaux de l'arborescence.
- ceci exprime une finalité
- une infinité de structure existe
- éviter la duplication inutile

Nous créons donc suite à caci un FAST (*truc le plus long au possible*) sous forme d'arbre de cette manière ci :

![[arbre.png]]

---
## <font color = pink> Ordonner les FS/C (p.151)</font>

>Ordonner : consiste à établir une liste ordonnée de l'ensemble des FS/C en y associant une propriété opérationnel

Cette table est celle qui permet de carathériser l'AFB $\rightarrow$ **LA TABLE LA PLUS IMPORTANTE** 
![[tableau-ordonner.png]]
Énoncé $\rightarrow$ c'est quoi ? 
La colonne commentaire est nécessaire $\rightarrow$ elle permet de lorsque nous revenons sur la table pour la comprendre 

Pour la colonne priorité, ceci est définie par une valeur de 1 à 4 par les critère, du point de vue de l'utilisateur suivants:
- P4 $\rightarrow$ vitale
- P3 $\rightarrow$ Essentiel 
- P2 $\rightarrow$ Confort 
- P1 $\rightarrow$ Luxe
---
## <font color=pink>Caractéristiques FS/C (p.156)</font>

<font color = red> /!\ ceci représente 80% du travail</font>

>Caractérisation : Quantification des performances attendues des FS/C au moyen de critères accompagnés d'une échelle permettant de situer le niveau de performance. 

Nous allons donc définir des bornes de satisfaction comprissent entre 0 et 100. Il faut aussi exprimer la Flexibilité :
- F0 : impérative $\rightarrow$ nécessaire donc 0 ou 1
- F1 : peu négociable  $\rightarrow \frac{100}{x^2}$   
- F2 : négociable $\rightarrow x$ 
- F3 : très négociable $\rightarrow x^2$ 
ceci permet donc de voir comment évolue la satisfaction dans l'intervalle. Pour déterminer ces critère, nous allons les pondérer, car ceci ne vas pas être le même pour un sous marin pour le déplacement, si il est en combat (peu négociable) ou si il prépare une embuscade(négociable).

Pour trouver les critères nous pouvons `réfléchir par l'absurde` et sont dans une liste (p.161)

**p.159**
N_REQ $\rightarrow$ TBD = à définir 
CdENV $\rightarrow$ ANY = ceci est conforme à tout les environnement

---
## <font color = pink> Ajuster les niveaux de performance (p.163) </font>

>Ajustement : Conciste à déterminer la valeur optimale des performances attendue  pour chaque FS/C 

c'est méchant industriel voudrons toujours faire les truc les plus faibles. 













