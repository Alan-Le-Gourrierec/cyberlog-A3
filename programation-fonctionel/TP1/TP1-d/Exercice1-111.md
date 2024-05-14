# Exercice 1 

### Exercice 1.1.1

```ocaml
let racine = function x ->if (x<0)
  then failwith "Erreur, division d'un nombre négatif"
  else sqrt(float_of_int(x));;
```
cette fonction permet de prendre en entré un int et retourne sa racine si et seulement si ce nombre est positif :
```ocaml
val racine : int -> float = <fun>
```

### Exercice 1.2.1

```ocaml
let hasard = function x ->
  if x>=0
  then x= Random.int 10
  else failwith "Erreur, la valeur de x est négative";;
let hasard = function x -> positif x = Random.int 10;;
```

cette fonction renvoie si oui ou non l'entier x est égale à la valeur choisie au hasard :

```ocaml
val hasard : int -> bool = <fun>
```

### Exercice 1.2.2

```ocaml
let expcos = function x -> 
    let cosx = cos(x) in
        exp(cosx*.cosx +.2.)-.10.;;
```

### Exercice 1.3.1

```ocaml
let discriminant = function a -> function b -> function c -> 
    let d = b*b-4*a*c in
    if d>0
    then 2
    else if d=0
    then 1
    else 0;;
```

### Exercice 1.3.2
```ocaml
let poste = function p -> function r ->
    match r with
        | 1 when p <= 20 && p>0 -> 0.50
        | 1 when p <= 50 && p>20 -> 0.78
        | 1 when p <= 100 && p>50 -> 1.18
        | 2 when p <= 20 && p>0 -> 3.33
        | 2 when p <= 50 && p>20 -> 3.61
        | 2 when p <= 50 && p>50 -> 4.02
        | _ -> failwith "Erreur, le poid ou la forme n'est pas valide";;
```




