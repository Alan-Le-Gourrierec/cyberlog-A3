[[exercice1-1]][[exercice1-2]][[exercice2-1]]
```ocaml
['a','b'];;
- : (char*char) list = [('a','b')]
```

```ocaml
let expz = fun x y -> (x 3)+.y;;
val expz : (int -> float) -> float -> float = <fun>
```

```ocaml
let test = [(function x -> string_of_float(x))];;
```
```ocaml
let x = [1.;2.;3.];;
let test = fun x -> string_of_float(x);;
```


```ocaml
let tmp = function f -> function x ->  f ;;
-: 'a->'b->'a =<fun>
```

```ocaml
let tmp = fun x y -> x = y;;
```