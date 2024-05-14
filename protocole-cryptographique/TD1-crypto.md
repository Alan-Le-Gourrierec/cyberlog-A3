### Exercice 1

- Q1 : authentification bionique 
- Q2 : signer numériquement un message pour l'authentification
- Q3 : VPN
- Q4 : Vérifier l'intégrité des données
- Q5 : SHA-256
	- bcrypte marche aussi mais car il est plus lourd il est moins utilisé (avantage asymétrique mais problème de )
- Q6 : Pare-feu
- Q7 : vérifier l'identité d'un site WEB
- Q8 : anti-virus 
- Q9 : clé publique 
- Q10 : authentification à deux facteurs 

## Exercice 4

### Question 1
![[Pasted image 20231201084438.png]]

#### comment ca marche ?

échange de clé => 
crypto symétrique : il n'y à qu'une seule clé. 
asynchrone => on utilise des nom et pas des estampilles (synchrone => ta, tb, .. tn)
avec serveur 

#### rôles

pour obtenir les rôles on recopie les lignes de A, B et S dans notre cas on remplace aussi le message par des variables

<u>exemple :</u>

<i> role de A </i>
1. A −→ B : M,A,B,{Na,M,A,B} kas
2. I(B) −→ A : M,{Na,<font color = cyan>X1</font>} kas

<i>role de B</i>
1. I(A) −→ B : M,A,B,<font color = cyan>X4</font>
2. B −→ I(S) : M,A,B,<font color = cyan>X4</font>,{Nb,M,A,B} kbs
3. I(S) −→ B :M ,<font color = cyan>X5</font>,{Nb,<font color = cyan>X6</font> } kbs
4. B −→ I(A): M,<font color = cyan>X5</font>

<i>role de S </i>

1. B −→ S : M,A,B,{<font color = cyan>X2</font>,M,A,B} kas,,{<font color = cyan>X3</font>,M,A,B} kbs
2. S −→ B :M ,{<font color = cyan>X2</font>,Kab} ka,{<font color = cyan>X3</font>, Kab } kbs

vérification de la série => regarder si on à bien tout et dire ce à quoi correspont X1,X2...Xn

---

## Exercice 5

1. A −→ B : A
2. B −→ A : Nb
3. A −→ B :{Nb }$_{kas}$
4. B −→ S: {A, {Nb }$_{kas}$ }$_{kbs}$
5. S −→ B: {Nb }$_{kbs}$

asynchrone / authentification /  serveur / unidirectionnel  / symétrique 

recherche de faille :
en trouvant une séquence valide qui prouve à B que I est belle et bien A

<i> role de A </i>

A −→ I(B) : A
I(B) −→ A : $X_1$
A −→ I(B) :{$X_1$ } kas

## Exercice 6

1. A −→ S : A,B,Na
2. S −→ A : {Na,B, Kab , { Kab ,A} Kbs } kas
3. A −→ B : { Kab ,A} Kbs
4. B −→A: {Nb} kab
5. A −→B: {Nb-1} kab

échange de clé/ serveur / asynchrone / bidirectionnel

1. A −→ I(S) : A,B,Na
2. I(S) −→ A : {Na,B, $X_1$ , $X_2$ } kas
3. A −→ I(B) : $X_2$
4. I(B) −→A: {$X_3$} $_{X_2}$ 
5. A −→I(B): {$X_1$-1}$_{X_2}$ 

<i>rôle de B </i>
1.  I(A) −→ B : { $X_4$ ,A} Kbs
2.  B −→I(A): {Nb} $_{X_4}$
3. I(A) −→B: {Nb-1} $_{X_4}$ 

<i> rôle de S </i>

1. A −→ S : A,B,$X_5$
2. S --> A : {$X_5$,B, Kab , { Kab ,A} Kbs } kas

### Trouver une attaque 

1. A --> S : A ,B,Na
2. S  --> A : {Na,B,Kab,{Kab,A}kbs
3. I −→ B : { K'ab ,A} Kbs}                 --------- B tombe instantanément dans le piège 
4. B --> I : {Nb}K'ab                            -------- 
5. A --> I B : {Nb-1}K'ab

## Exercice 2


