# Complexité et notation

- calculer le nombres d'opérations 
- n == taille des données
    - elle peu être un constante 
    - variable 
    - elle représente le nombres maximal d'itération de l'lago
> elle représente le nombres d'itération maximum que le programme devras efectuer.

**O représente la complexité de la fonction** 

---
_exemple_ :

f(n) = n² + 2n + 1  => O(n²)
pour déterminer C maintenant, nous allons majorer nos variables => f(n) = n² + 2n² + n² = **4**n² ce qui veux dire que c = **4**

--- 

Nous déterminons donc un majorant pour déterminer avec la plus petite croissance. elle peuvent être de : 
- O(k)
- O(log(n))
- O(n^n)
- O(n.log(n)) ...
> forte influance de la complexité sur le temps de l'algoritmes, avec complexité exponanciel, ceci peu prendre des milénaire si pas 
---
un **invariant** est l'opération éfectué par le programe, par exemple, dans le programme somme, nos invariant sont nos variable : i et sum 

| Étapes | i | Sum |
:---:|:---:|:---:
0 | 1 | S(k=0 à i-1) A[k] = A[0]
1 | 1 | A[0]
2 | 2 | S(k=0 à i-1) A[k] = A[0] + A[1]
