aléatoire ?

## ptdr c koi

soumis au hasard 
notion d'équiprobabilité
valeurs équiprobable et pas prédictible avec les éléments précédent

annalyser un lancer de pièces c du shnapss en barquette on utilise que le ms de l'ordi 

- la suite dois être déterministe, même data + même paramètre => même chose
- reproductible
- fréquence d'aparition identique
- facile à mettre en oeuvre 
- rapide

GPA générateur pseodo aléatoire 

$S_0$ est la seed. 
f fonction génératrice 
U ensemble des nombre de sortie 
g fonction de sortie

## divers GNA

GCL (générateur congruenciel linéaire) => 

S=[0,1,...m-1]
$f(s) = as +b [m]$ 
U=[0;1[
$g(s) = \frac{s}{m}$

Ultimement périodique inclu périodique (ultimement périodique, qui fini par être périodique)

GMR (générateur multi récursif)

$S=\{0,1,...m-1\}^k$
$f(s)=f(s^{(1)},s^{(2)},...s^{(k)})$
U=[0;1[
$g(s)=\frac{s^{(k)}}{m}$

générateur digitaux 

$S = {0,1}^k$
$f(s)= A \times s$
U=[0,1[
$g(s) = ((Bs)_i[2])*2^{-i}$

## test sepctral 

test sepctrale à une dimension 

OMG il y à 3 dimestions et on va devoir les tracer avec 2 dimenstions 

on peu le faire en 4d mais ptdr komant tu le vois ???? => tu met des métriques 