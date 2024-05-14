```Ocaml
let a=1 in
let a=2 and b=a in
a+b;;
```
> -: int = 3
a;;
>Error : Unbound value a 

let a = 42;;
>val a: int = 42

let a = a/ 2;;
>val a: int = 21

```Ocaml
let b x =
let a = float_of_int a in
a ** x;;
```
>val b : float -> float = \<fun>

b 1.;;
> -: float = 21.
let a = -3;;
>val a: int = -3
b 2.;;
> -: int = 441 (du à 21**2)
```Ocaml
let f1 x y = if x < 0
then x-y
else x+y;;
```
> val f1 : float -> float -> float

f1 a (int_of_float (b 5.));;
> -: int = -4084104

f1 -4 a;;
> Error : 

f1 (-4) a;;
> -: int = -1

let f x = log (float_of_int x) /. log 2. ;;
>val f : int -> float \<fun>

f f a;;
>Error

f (f a);;
>Error
