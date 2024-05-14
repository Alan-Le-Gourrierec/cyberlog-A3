```ocaml
let h(f,g) = function x -> f(g x);;
```

nous avaons dans un premier temps : tf*tg -> tx -> tres 
>or f et g sont des fonctions donc : <br>

(tfe -> tfs) * (tx -> tgs) -> tx -> tres <br>
<=> (tfe -> tres) * (tx -> tfe) -> tx - tres <br>
Nous obtenons donc finalement : ('a->'b) * ('c-> 'a) -> 'c -> 'b

---
```ocaml
 let i(a,b,c) = function x -> (a b (c * x));;
```

nous avons : $(t_a * t_b * t_c) \rightarrow t_x \rightarrow t_{res} $


>or nous avons (c * x) => type = int :

$(t_{ae} -> int) * (int -> tae) * int -> int -> int$ <br>
(tb -> 'b) * ('a -> int) * (int->int) -> int -> 'b <br>
=> ('a -> int -> 'b) * ('a -> int) * int -> int -> 'b <br>

---
```ocaml
let j a b c = if (a>1 || c) then (b c a) else (a,c);;
```
$t_a \rightarrow t_b \rightarrow t_c \rightarrow t_{res}$ <br>
or nous avons a qui est un int et c qui est un bool donc : <br>
$int \rightarrow (tc \rightarrow int \rightarrow (int \rightarrow t_c)) \rightarrow t_c \rightarrow (int * t_c)$ <br>
$int \rightarrow (bool \rightarrow int \rightarrow (int \rightarrow bool)) \rightarrow bool \rightarrow (int * bool)$ 