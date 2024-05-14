```ocaml
let pronom = fun pluriel numero -> 
    match pluriel,numero with  
    | true,1 -> "je"
    | true,2 -> "tu" 
    | true,3  -> "illeon" 
    | false,1 -> "nous" 
    | false,2 -> "vous" 
    | false,3    -> "illes"
    | _ -> failwith "Erreur, les valeurs ne sont pas correct";;
```
$val : pronom \rightarrow bool \rightarrow int \rightarrow string = <fun>$ 
```ocaml
let premier_groupe = fun werbe ->
    let len = String.lenght verbe in
```
