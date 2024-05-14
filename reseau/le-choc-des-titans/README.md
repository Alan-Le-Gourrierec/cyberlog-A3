# Sujet 7 - Le choc des titans 

## Auteurs:

- Joseph de l'Estourbeillon
- Alan le Gourrierec
- Ewan Pallavicini

***
***

## Détails:

### Machine A - La victime qui attaquait

#### Alan : Voici le détail de mes programmes:

Le programme `founds.sh` permet de scanner le réseau afin de déterminer les divers personnes présente sur ce dernier dans le but de pouvoir appliquer le second programme `MITM.py`.

Ce second programme, lui permet d'intercepter les communications entre deux personnes. Dans notre cas, ceci sera entre B et C respectivement, Ewan et Joseph. Pour ce faire, nous envoyons une requet ARP stipulant que je suis Ewan pour Joseph et que je suis Joseph pour Ewan. Par cette manipulation, je peux obtenir les communications entre ces deux personnes.

Si je suis détecté, mon but est de répondre, pour ce faire, je souhaite toujours avoir accès à leurs communications. Je change donc mon adresse MAC sur l'interface en question (dans notre cas, wlan0) avec `mac-addresse.sh` et relance le programme `MITM.py` pour écouter à nouveau ces conversations.

Dans l'autre cas, je souhaite pouvoir répondre en a la personne qui souhaite bloquer ma table ARP. Pour répondre à ceci, je sature son réseau avec `reponse.py`.


*** 

### Machine B - L'incassable et la balance ! (Joseph)

#### Voici les details de mes programmes :

Mon objectif est de détecter si il y a une attaques **M**an **I**n **T**he **M**iddle entre moi (machine B) et Ewan (machine C) par Alan (Machine A). Pour le détecter, je compare les entrées de la table ARP et je cherche si il y a 2 entrées avec une même adresse MAC mais deux adresses IP différentes. Ensuite, je fais un scan ARP avec Scapy. J'ai remarqué qu'en envoyant une requête en broadcast à une machine, c'était la bonne adresse MAC qui m'était retournée. De cette manière, je peux voir quel est la machine qui attaque, car je vois quelle est la machine dont l'adresse MAC à été usurper par l'adresse MAC de l'attaquant.

Après avoir détecté l'attaque, je supprime l'entrée de l'attaquant de ma table ARP, puis je fais un pare-feu pour bloquer tous les paquets venant de l'attaquant. Je crée le pare-feu à l'aide de la commande `arptables`, car je n'arrivais pas à faire un pare-feu fonctionnel avec `iptables`.

#### Prérequis:

Pour faire fonctionner le programme, il est nécessaire d'avoir :
- une machine avec un noyau unix (donc pas windows)
- les droits administrateur (sudoer)
- python3
- bibliothèque scapy
- la commande système `arptables`

#### Comment faire fonctionner mon programme:

- Lancer la communication avec le serveur (%achine C):
	```shell
	python3 client.py
	```
- Lancer le programme principal puis supprimer ou non les adresses mac suspects :
	```shell
	sudo python3 MITMProtector.py
	```


***

### Macine C - Le catcheur

#### Ewan : Voici le détail de mes programmes :

Le programme `pingGentil.py` permet d'ouvrir un canal de discussion dans lequel on peut entrer des messages avec Joseph dont je suis l'hôte et il est le client. Dans la même idée, le programme `pingPong.py` envoie toutes les 2s ping, et l'autre pong 2s après quand il le reçoit etc.

Dans le vif du sujet, j'ai le programme `arpPoisoning.py` qui peut bombarder une adresse en lui mettant à jour en boucle sa table arp en spécifiant que sa gateway est lui-même. Comme c'est l'adresse du routeur, il ne peut plus tenter d'accéder à des paquets en dehors du réseau. Je fais la même chose par rapport à son addresse dans la table arp du routeur.

J'ai ensuite le programme getArp qui enregistre cette dernière dans un fichier, puis en le lisant et grâce au regex, je le fait matcher avec un pattern qui récupère l'adresse ipv4 et l'adresse mac quand le type d'adressage est dynamique (en réalité j'enregistre aussi le type, qui est tout le temps dynamique, ce n'est pas nécessaire mais je le garde pour des raisons de debuggage pour vérifier avec un print que toutes les adresses sont bien dynamiques).

Ainsi, si je repère qu'un adresse mac possède 2 ou plus adresses ipv4 sur le réseau, il y a sûrement un man on the middle, donc je l'affiche à l'utilisateur et j'effectue le arp spoofing avec pour cible cette adresse.

***
