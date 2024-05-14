[[exercice1-1]]
let rac_pi = sqrt(22/7);;
>la fonction comme tel ne fonctioneras pas, sqrt est une fonction associé au decimaux, il faut donc convertir nos valeur et opérande dans les decimaux 
```ocaml
let rac_pi = sqrt(float_of_int(22)/.float_of_int(7));;
```
1/2 = 0;;
>ceci va être vrai pour tous les cas car 1/2 reveras 0 car ceci fais la division entière or le quotiens de cette opératiob est 0 donc nous aurons : -: bool = true

let pair = function n -> 2*(n/2) = n;;
> la fonction est correct 

let a = 4.0;;
> val a: float = 4.

let b = 4.0;;
> val b: float = 4.

let c = 1.0;;
> val c: float = 1.

let delta = b*.b -. 4.0*.a*.c;;
> ceci permet de calculer le discriminant du polynôme formé par a,b,c et ceci renvoie : val delta: float = 0.

```ocaml
let s1 = if delta >= 0.0
    then ((sqrt delta) -. b)/.a/.2.0
    else "pas de solution"
and s2 = if delta >= 0.0
    then ((sqrt delta) +. b)/.a/.2.0
    else "pas de solution";;
```
> ceci renvoie une erreur car le else renvoie un string et non un float comme ceci est nécéssaire du au typage stricte de Ocaml

```ocaml
let s1 = if delta >= 0.0
    then string_of_float(((sqrt delta) -. b)/.a/.2.0)
  else "pas de solution"
  and s2 = if delta >= 0.0
    then string_of_float(((sqrt delta)+. b)/.a/.2.)
  else "pas de solution";;
```
>Ceci permet d'obtenir un string à la sortie peu importe ce qui se passe 


let entier = function x -> float_of_int (int_of_float x) = x;;
> fonction "entier" qui renvoie si oui notre nombre est entier, si non il est flotant

```ocaml
let oups = function num ->
    if (entier num)
        then int_of_float num
    else num;;
```

```ocaml
let oups = function num ->
  if(entier num = true)
  then string_of_int (int_of_float num)
  else string_of_float(num);;
```
>converti le resultat vers un entier et le convertie en string pour "normaliser" la sortie


```ocaml
let f = function n -> 2*n;;
let g = function n -> n+n;;
```
>implémentation des deux fonction : f et g qui permetent de faire concrètement la même chose, elle pernnent un int et renvoie deux fois ce même int 

f = g;;
>cecie renvoie une erreure, car nous comparons duex fonction, pour régler le pb, il suffit de leur donner la même valeur et de comparer ses valeurs.

(f 2) = (g 2);;
>implémentation de la solution proposé précédement (et ceci renvoie : -: bool = true)

```ocaml
let bencaalors =
bencaalors 8;;
bencaalors 10;;
bencaalors 40;;
function n -> if (exp (float_of_int n) *. (log 10.0))
<>
(exp (float_of_int n) *. (log 10.0)) +. 1.0
then "tout va bien"
else "euh ...";;
```
>ben mon reuf c out of range (max 2³⁰-1)
