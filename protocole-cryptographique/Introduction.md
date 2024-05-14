alor[[Generalite-et-rappels]]

>**protocole** : séquence d'étape de communication et de calcule ou nous chiffrons le message 
>**protocole cryptographique** : protocole qui se base sur la cryptographie 

nances : Nbr synchrone (si t$_ A$ = t$_B$ ) / si asynchrone => nbr aléatoire 

Rôle 

> **principale** : participe à la section
> **nance et timestap** : permet de vérifier la "fraîcheur" du message

---

Sécurisé => conserver son identité secrète  sans qu'elle ne fuit (Confidentialité)
Authentification du message => vérifier l'intégrité du message 

ceci créer donc des protocoles cryptographique plutôt logique afin de s'assurer de la signature de l'autre partie $\Rightarrow$ grâce à un source de confiance 

---
Protocole Needham Shroeder, basé sur des clé assymétrique

## <font color = orange> Protocole d'échange de clé </font>
(protocole de distribution de clé)

afin de distribuer les clé il y à solutions :
- envoyer directement la clé en crypté à B 
- envoyer à une entité de confiance (pas à Johane de merde)

protocole Carlson / protocole diffie-hellman, LE RETOUR DE BOB ET ALICE !!!

**Certificat numérique** : contiens la clé numérique et les infos sur l'identification publique des entités 

## <font color = orange> Failles des protocoles </font>

protocole = algorithmes distribué avec plusieurs participants.

Rôle abstraction du protocole ou l'emphase est mise sue un principal donné.

---
```LaTeX
A => B : A
B => A:N$_b$
A=> B:N$_b$ :(N$_b$)k$_b$
B => S : (A(N$_b$)k$_b$)b$_{ab}$ 
S => B : (N$_b$)k$_{ab}$
```
---
```LaTeX
Rôle de B
I(A) => B : I(A)
B => I(A):N$_b$
I(A)=> B:N$_b$ :(N$_b$)k$_b$
B => I(S) : (I(A)(N$_b$)k$_b$)b$_{ab}$ 
I(S) => B : (N$_b$)k$_{ab}$
```
---

> trace = exécution valide d'un protocole => tout les agents honnête y participent se comportent conformément à la spécification du protocole
> tout les messages envoyé par l’intrus 

#### Modèle d'intrus DY
C'est un mec super fort avec un gros cerveau qui possède un max de cash et de perf (pas l’œil gauche de joseph). Capacité de mémoire infini et connaissance parfaite en terme logique 

- faille de fraîcheur 
- faille d'oracle 
- faille d'instanciation 

## <font color = orange> Vérification du protocole </font>

Logique boléen 

P | $\equiv$  
