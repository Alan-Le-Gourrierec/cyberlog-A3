```ocaml
let bisextile = function a -> 
let d = a mod 4 in
    match d with
    | 0 when a mod 100 <> 0 || a mod 400 = 0 -> true
    | _ -> false;;
```
