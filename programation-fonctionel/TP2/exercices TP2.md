# Exercice 1

```ocaml
let rec somme f m n = if m > n then 0
else (f m) + (somme f (m+1) n);;
```

>Cette fonction somme prends en entré m et n qui sont des entiers donne en sortie un entier. Pour le cas de f, ceci est une fonction qui prends en entré un int et renvoie un int:
>elle borne notre fonction avec une boucle if qui dit que tant que $m>n$ ceci nous renvoie 0, sinon elle nous renvoie somme de $m+1$ ce qui permet que dans $m = n \rightarrow$ ceci coupe

$val  somme =(int \rightarrow int) \rightarrow int \rightarrow int \rightarrow int = <fun>$

### Exercice 1.1 (modélisation de $\sum$)

1. Dans le premier exemple, il nous suffit de définir f comme étant la fonction identité et nous obtenons la fonction suivante :

```ocaml
let n = 4;;
let identity = function n -> n;;
```
>- :  int = 10
2. La deuxième question est identique à la premier, il nous suffit de réutiliser la fonction identité.
```ocaml
let m = 2;;
```
> - : int = 9 (test pour 2 à 4)
4. Dans cette 3$^e$ question, il nous suffit de faire une fonction qui prends en entrer un en entier n et renvoie sa valeur au cube :
```ocaml 
let m = 1;;
let cube = function n -> n*n*n;;
```
> - : int = 100 (test pour 1 à 4)

4. Pour cette dernier question, il faut faire une fonction récursive qui renvoie la factoriel de n (donc en récursif) :
```ocaml
let rec factoriel = function n ->
	if n = 1 then 1
	else n * factoriel (n-1);;
```
>- : int = 33 (de 1 à 40) 
---
### Exercice 1.2 (récursivité sur les chaînes de caractères)

Dans un premier temps, nous exécutons les divers fonctions dans l'exercice puis nous exécutons les fonctions suivantes :
```ocaml
#trace occur;;
occur "120004009";;
```
1. Nous obtenons donc : 
```ocaml
occur <-- "120004009"
occur <-- "20004009"
occur <-- "0004009"
occur <-- "04009"
occur <-- "4009"
occur <-- "009"
occur <-- "9"
occur raises Invalid_argument "String.sub / Bytes.sub"
occur raises Invalid_argument "String.sub / Bytes.sub"
occur raises Invalid_argument "String.sub / Bytes.sub"
occur raises Invalid_argument "String.sub / Bytes.sub"
occur raises Invalid_argument "String.sub / Bytes.sub"
occur raises Invalid_argument "String.sub / Bytes.sub"
occur raises Invalid_argument "String.sub / Bytes.sub"
Exception: Invalid_argument "String.sub / Bytes.sub".
```

2. nous voyons donc que la fonction **occur** est exécute 7 fois et ceci nous renvoie une erreur. 
3. Si nous regardons à la dernier exécution de la fonction **occur** (7$^e$) nous obtenons une erreur car nous avons 9 et donc ceci n'est pas un zéro $\rightarrow$ nous passons au deuxième cas, c'est à dire :
```ocaml
let rec occur y =
match y with
	| "" -> 0  (*premier cas*)
	| _ -> let ch1 = cdr y in (*deuxième cas*)
		let ch2 = cdr ch1 in
		if String.sub y 0 2 = "00" (*problème*)
		then 1 + occur ch2
		else occur ch1 ;;
```
le problème est que nous passons en "out of range" et ceci crée donc un bug.
4. Pour fixer le problème, il nous suffit de faire :
```ocaml
let rec occur y =
match y with
	| "" -> 0
	| y when String.length(y)<2 -> 0
	| _ -> let ch1 = cdr y in
		let ch2 = cdr ch1 in
		if String.sub y 0 2 = "00"
			then 1 + occur ch2
		else occur ch1 ;;
```

#### Miroir

```ocaml
let rec string_to_char_list s = match s with
	| "" -> []
	| n -> string_to_char_list;;

let rec miroir s = let len = String.lenght(s), L=[] in 
	if len = 0 then " "
	else T(len)::L 
```


---
### Exercice 1.3 (les nombres premiers)
#### Question 1

nombre premiers :
```ocaml 
let max = fun a b -> match a,b with
	| _ when a-b>0 -> a
	| _ when a-b<0 -> b
	| _ -> a;;

let min = fun a b -> match a,b with
	| _ when a-b >0 -> b
	| _ when a-b < 0 -> a
	| _ -> a;;
	
let rec div_between = fun a b n -> let c = max a b in let d = min a b in
	if d = c || n mod d = 0
		then n mod d = 0
	else div_between (d+1) c n;;
```

#### Question 2
```ocaml
let  prime = fun a -> let tmp = int_of_float(sqrt(float_of_int(a))) in
	if a >= 0 then
		div_between 2 tmp a 
	else failwith "la valeur de a est nagétive";;
```

#### Question 3
```ocaml
let no_div_from = fun a n -> let tmp = int_of_float(sqrt(float_of_int(a))) in
	if a > tmp 
		then div_between 2 tmp n
	else div_between 2 a n;;
```




