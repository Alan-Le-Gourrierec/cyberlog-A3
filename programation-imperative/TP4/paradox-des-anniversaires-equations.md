## Démonstration
On pose : <br>
$H1(x)=\sum_{i=0}^n chr(i)*256^i$ <br>
$h:x\rightarrow (H1(x) mod(255))$ 

Nous souhaitons démontrer que peu importe l'odre des lettres dans un mot, avec cette fonction, pour démontrer ceci, nous allons utiliser le petit théorème de Fermat qui nous dis : <br>
$a^p \equiv a[p] \Rightarrow a^{p-1} \equiv 1[p]$ <br>
Dans un premier temps, nous remrquons que : $PGCD(256,255)=1$ 

## Paradox des anniversaire 
Le <font color = orange>paradox des anniversaires </font> déterminé la probabilité, celon un certain nombre de personne (et dans une année non bisextile), la probabilité que deux personne possède la même date d'anniversaire. <br>
Pour exprimer ceci, nous allons déterminer la probabilité que deux personne n'aient pas la même date de naissance et utiliser le propriété suivante après : <br>
$P(\bar{A}) = \frac{365!}{(365-k)! * 365^k}$, $\forall k \in \mathbb{N} \land 1\leqslant k \leqslant 365$ <br>

Il nous suffit donc d'utiliser la propriété de probabilité suivante : <br>
$P(A) =  1 - P(\bar{A})$

## Intéret de cette fonction pour le hashage
Cette fonction, déterminant la probabilité que deux personne soient née un même jour. Si nous changeons le nombre de jour d'une année par la taille de nos chaîne (dans l'exercice 3) et que nous remplacons k par le nombre d'itération, nous obtenons les probabilités d'avoir une colision. <br>
La généralisation de cette fonction est donc : <br>
$P(\bar{C}) = \frac{size!}{(size-i)!*size^{i}}$,$\forall (i,size)\in\mathbb{N}^2\land 0\leqslant i\leqslant size$ <br>
(avec size : la taille de la chaîne, i : le nombre d'itération)

