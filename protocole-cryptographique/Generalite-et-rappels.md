## <font color = green> I - Rappels </font>

#### <font color = green> 1- Symétrique </font>

Cesar (et décalage pour  tout n $\neq$ 3 $\Rightarrow$ Cesar)
chiffrement affine (avec une fonction)

#### <font color = green> 2 - asymétrique </font> 

RSA [[TP RSA.pdf]] clé privé et clé publique 

>clé différente pour le chiffrement et le déchiffrement  

- cryptage par bloc $\Rightarrow$ RSA, 3DES  encodage de toutl le bloc en un coup 
- cryptage par flux $\Rightarrow$ RS4 et Salasa20 par partie
- cryptage par seuil $\Rightarrow$ ECC, Kwartzyk prérequis 
- cryptage quantique $\Rightarrow$ E91, BB84 changement rapide de la clé

> fonctions de hachages : possède une trace de fonction (taille fixe, rapide à calculer, irréversible) en MD5, SHA1, SHA2, SHA3

## <font color = red> second cours </font>

>Protocole cryptographique => ensemble de technique aidant à crypter le message dans le but de garantir la confidentialité  des échanges. C'est des ptn des rappels ... c'est chiant 

trouvable dans les communication, la sécurisation des données, les payements, les OSs. <br> Le choix entre les deux algos est de : pour le chiffrement symétrique est plus rapide et la question se pose de comment partager la clé, ce qui créer un problème de sécurité. Un des avantages de l'asymétrique, pour une quantité importante de donnée, ceci est plus lourd cependant ceci est plus sécurisé par l'utilisation de clé privé et publique. 

exemple page 9 : RSA ou Bob et Alice génères une clé 

exemple : Alice prends a = 8 et bob prends b = 13 (p = 23 et g = 7)

A = $g^a mod 23$ ; B $g^bmod23$ 
Ils vont tout les deux obtenir 6 

Pour se faire, il existe divers attaques possibles:
- man in the middle 
- brute force 
- recherche exhaustive (logjam)

#### <font color = green> Otway protocole </font> 

2 entiter A et B 

- A et B deux participants 
- $K_{as}$ et $K_{bs}$ deux clées secrètes partagé avec S 
- M est l'identifiant de la section, $N_a$ et $N_b$ des nances (variables temporiares)
Cf(protocole page 16)

Attaque d'interception avec Man in the middle. 

Pour se faire, il suffit d'intercepter une des clée entre A et B et envoyer des messages à la place de B et recevoir les réponses à la places de A. 

- A -> B : M,A,B ($N_B$, M, A,B)$K_{as}$
- B -> S : M, A, B,{$N_a$,M,A,B}$K_{bs}$ ($N_b$ , M, A,B)$K_{ab}$ 
- D -> récupération de $K_{ab}$ -> possibilité de décrypter  les message entre A et B = problèmes

#### <font color = green> Protocole Needham-Schroeder (1978) </font>

![[Pasted image 20231113172721.png]]

faille réception man in the middle **encore** ... 

#### <font color = green> processus Kerberos </font>
demande d’authentification au serveur d’authentification, il va lui retourner une clé pour communiquer avec les TGS avec les infos de l'adresse du serveur TGT(elle aura aussi une date d'expiration). 
Dans un second temps, le client va envoyer le ticket et le timestamp. Il enverras aussi la clé pour déchiffrer le paquet. Le TGS s'assure que le client est bon il va donc envoyer en retour les information du service chiffré 

(doc)[https://www.pingidentity.com/fr/resources/identity-fundamentals/authentication-authorization-protocols/kerberos.html]

## <font color = yellow> communication sécurisé </font>
- SSL/TLS (le seul que l'on va voir)
- IPsec

> SSL/TLS : protocole de sécurisation web -- SSL v1 1994
> SSL v2 1995
> SSL v3 1996
> 1999 pour TLS 

la sécurisation est assuré par le protocole de Record elle interviens entre la couche application et TCP :

- demande d’authentification
	- grace à un certificat 
	- le serve prouve qu'il en est propriétaire (avec la clé privé)
- authentification du client 
- Handshake => 
	- proposition d'une liste de clé entre client et serveur
	- sélection par le serveur d'une des clés et retourne son choix au client 
	- il se partagent la clé chacun l'un et l'autre 
- partage de la clé entre le serveur et le client 

Tout communication dois être crypté pour éviter les attaques de rejeu. 

	cf slide 43

