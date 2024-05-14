let f = function x -> x + 1;;
>definition fct

f 1;;
>-: int = 2

f (f 1);;
>-: int = 3

let f = function x -> function y -> x + y;;
>def fonction qui fais la somme de deux entiers

f 1 2;;
>-: int = 3

let g = function x -> (f x);;
>def fonction qui call f et qui fais la somme de x

g 45 2;;
>-: int = 47