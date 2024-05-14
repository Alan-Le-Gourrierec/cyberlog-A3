[[Module3.pdf]]
![[programme.png]]

Nous allons donc réaliser l’ingénieure des solutions, nous faisons normalement l'AOT et l'AFT en parallèle.

## <font color = cyan> Établir les Schéma technique statiques (p.8)</font>

> FT (Fonction Technique) : action interne au produit définie pour assurer une ou plusieurs Fonction de Service et/ou Contraintes

Type de flux | Représentation
---|---
Signale/information | flèche complete 
Énergie | flèche en pointillé 
Matière | flèche à double traits 

on peu la nommer de deux manière différentes :
- mettre un nom
- mettre sous forme de "verbe + complément"

Pour réaliser les schéma, se référer au pages 11 et 12. 

>NDA (niveau d'abstraction): Correspond au rang de définition des FT, par convention, le niveau du Produit est appelé N0.

- approche Top/Down
- il n'y à pas de conventions, cela dépends :
	- du concepteur (son expertise, sa créativité ...), il va chercher à être précis (exemple comment ça se déroule au niveau du protocole, pas de liberté) $\rightarrow$ le plus bas possible 
	- du sujet traité

> CF (Chaîne Fonctionel) : Regrouper un ensemble de FT interconnecté entre elles afin de réaliser une action globale.

- définition plus détaillé de la NDA N$_{i+1}$ 
- départagé en 3 sous-ensemble :
	- sous-ensemble de l'aquisition
	- sous-ensemble pour le traitement 
	- sous-ensemble pour l'action

> TDC(Type de conception) : permet de distigué les différent dommaines technologiques utilisé en conception.

-| Générique 
---|---
A | Mécanique 
B | Optique 
C | Hydraulique/Pneumatique
D | Électricité
E | Électronique 
... | ...
*cf page 17*

> AL (architecture logique) : regroupe l'ensemble des principes de fonctionement **imaginé** au travert des différents Type de Conception concernée et **structurée** selon des NDA.

- pour répondre à des attentes, nous devons normalement créer plusieurs solution 

>STS(Schéma Technique Statique) : figure sous forme symbolique permetant de représenter les FT de manière statique.

<font color = red> /!\ FAIRE BIEN LA CARTOUCHE </font>
![[cartouche$.png]]
TDC = type de conception, le F TDC 
Titre et NDA nécéssaire 

---
IL Y 12k symbole de ses morts HAAAAAAAAAAAAAAAAAAAAAAAAA (cf Module 3 p.23-28)


### <font color = cyan> Mode et fonctionement </font>

> Commande d'une FT : entré spécifique d'une FT qui agit sur la manière de générer la sortie à partir de l'entrer 
> - On/Off
> - sens trigo/ sens horaire 
> - sens monté/ sens descendante 

>type contrôle => chef
>type opérande => personne qui exécute les ordres

<font color = red> ON NE PEU PAS AVOIR une FT qui possède 2 rôle (contrôle et opérande) => on la divise en 2 </font>

> Mode de fonctionnement (MdF) : comment les fonctions technique interagissent  ensemble dans le même niveau d'abstraction. 

> schéma des MdF (SMF)

### <font color = cyan> Table des FT </font>

> Table des FT regroupe toute les fonctions technique que nous avons identifier.

- Verbe + complément
- représenté dans un schéma STS ou STD
- nous pouvons représenter plusieurs fois une fonction technique

> caractérisation de FT : qualification des performances au moyen de critères techniques

![[Pasted image 20231122164714.png]]
