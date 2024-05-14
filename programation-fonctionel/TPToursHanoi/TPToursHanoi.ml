(***** Exercice 1.1 (préliminaires) *****)

(* Question 1 *)

type hanoi = { t1 : int list; t2 : int list; t3 : int list};;
;;


(* Question 2 *)

let tour1 = [1;4] ;; 
let tour2 = [2];; 
let tour3 = [3;5;6];;
let tour3bis = [5;3;6];;
let jeu1 = {t1 = tour1; t2 = tour2; t3 = tour3};;
let jeu2 = {t1 = tour1; t2 = tour2; t3 = tour3bis};;
let jeu3 = {t1 = [1;2;3;4]; t2 = []; t3 = []};;


(* Question 3 *)

let rec check t1 = 
        match t1 with
        | [] -> true
        | t::r when r = [] -> true
        | t::r when t >= (List.hd r) -> false
        | t::r -> check r;;


(* Question 4 *)

let make p1 p2 p3 = 
        assert (check p1 && check p2 && check p3);
        {t1 = p1; t2 = p2; t3 = p3};;

(* Question 5*)
let rec make_list_aux n table = 
        match n with
        | 0 -> table
        | _ when n < 0 -> table 
        | _ -> make_list_aux (n-1) (n::table);;

let make_list n = make_list_aux n [];;


(***** Exercice 1.2 (affichage) *****)

(* Question 1 *)
let hd_tl_opt lst = 
   match lst with 
   | []		-> (None, []) 
   | x::l	-> (Some x, l)
;;

let rec combine_aux lst1 lst2 lst3 res = 
        let a = hd_tl_opt lst1 in 
        let b = hd_tl_opt lst2 in 
        let c = hd_tl_opt lst3 in
        if fst a = None && fst b = None && fst c = None
        then res
        else combine_aux (snd a) (snd b) (snd c) ((fst a,fst b,fst c)::res);;
                                        

let combine lst1 lst2 lst3 = combine_aux (List.rev(lst1)) (List.rev(lst2)) (List.rev(lst3)) [];;

(* Question 2 *)
let print_option = function 
        | None   -> Printf.printf "   "
        | Some i -> Printf.printf "%3i" i;;

let rec print_options_list lst = 
        match lst with 
             | [] -> ()
             | (t1,t2,t3)::r -> print_option t1; print_option t2; print_option t3; print_string("\n"); print_options_list r;;
    
(* Question 3 *)

let print_hanoi hanoi = print_string("\n"); print_options_list (combine hanoi.t1 hanoi.t2 hanoi.t3); print_string("============");;


(* Question 4 *)

let rec print_hanoi_list hl =
        match hl with
        | [] -> ()
        | t::r -> print_hanoi t; print_hanoi_list r;;


(***** Exercice 1.3 (résolution) *****)
(* Question 1 *)
let move ls1 ls2 =
  match ls1 with
  | []       -> ls1, ls2
  | x :: ls1 -> ls1, x :: ls2

(* Attention : la fonction "play" est de type "hanoi -> int -> int -> hanoi". *)

let play {t1; t2; t3} src dst =
        match dst,src with
        | 1,2 -> t1,t2 = {t1 = fst(move t1 t2); t2 = snd(move t1 t2); t3 = t3}
        | 1,3 -> t1,t3 = {t1 = fst(move t1 t3); t2 = t2; t3 = snd(move t1 t3)}
        | 2,1 -> t2,t1 = {t1 = snd(move t2 t1); t2 = fst(move t2 t1); t3 = t3}
        | 2,3 -> t2,t3 = {t1 = t1; t2 = fst(move t2 t3); t3 = snd(move t2 t3)}
        | 3,1 -> t3,t1 = {t1 = snd(move t3 t1); t2 = t2; t3 = fst(move t3 t1)}
        | 3,2 -> t3,t2 = {t1 = t1; t2 = snd(move t3 t2); t3 = fst(move t3 t2)}
        | _,_ -> ();;

(* Question 2 *)
(*
let rec compute_aux n src dst aux res =
  if n = 0 
  then ... 
  else
      (* à la fin on déplace n-1 disques de aux vers dst *) 
      ...
      (* juste avant ça on déplace 1 disque de src vers dst *) 
      ...
      (* avant ça on déplace n-1 disques de src vers aux *) 
      ...
;;
*)
(*
let compute n src aux dst = 
;;
*)


(* Question 3 *)
(*
let rec apply_acc hanoi moves acc =
;;
*)
(*
let apply hanoi moves = 
;;      
*)
		
(* Question 4 *)		
(*
let hanoi_towers n =
;;
*)
