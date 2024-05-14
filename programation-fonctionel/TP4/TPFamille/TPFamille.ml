(* Question 1 : Création des données *)

let p1 = ("Etogo","Se");;
let p2 = ("Se","Mafo");;
let p3 = ("Togo","Bogo");;

let pop1 = [("Se","Mafo");("Togo","Bogo");("Zogo","Mboyen")];;
let pop2 = [("Etogo","Se");("Se","Mafo");("Mafo","Ekwikwi");("Ekwikwi","Zogo");("Zogo","Mboyen")]
let liste_lignages1 =[["Etogo"; "Se"; "Mafo"; "Ekwikwi"; "Zogo"];
["Se"; "Mafo"; "Ekwikwi"; "Zogo"];
["Mafo"; "Ekwikwi"; "Zogo"];["Ekwikwi"; "Zogo"];
["Zogo"]];;

(* Question 2 : Prédicat "a_un_pere" *)
let rec a_un_pere personne population = 
        match population with
        | [] -> false
        | (p,_)::r when p = snd personne -> true 
        | _::r -> a_un_pere personne r;;

(* Question 3 : Fonction "pere" *)

let rec pere personne population = 
        match population with
        | [] -> failwith "La population ne contient pas de pere."
        | t::r when fst t = snd personne -> t 
        | _::r -> pere personne r;;
      
(* Question 4 : Fonction "lignage" *)
(*let rec listepere personne population tabular =
        match population with
        | [] -> snd personne::tabular; fst personne::tabular 
        | (p,s)::r when p = snd personne -> listepere personne r (tabular::s)
        | _::r -> listepere personne r tabular;;
*)
let rec lignage_aux pers pop res =
        if (a_un_pere pers pop)
                then(lignage_aux (pere pers pop))
                pop(List.append res[snd pers])
        else List.append res [snd pers];;


let lignage pers pop = lignage_aux pers pop [fst pers];;

(* Question 5 : Fonction "dernier" *)

let dernier l =List.hd(List.rev(l));;

(* Question 6 : Prédicat "frere" *)

let frere p1 p2 population = dernier (lignage p1 population) = dernier (lignage p2 population);;

(* Question 7 : Fonction "liste_lignages" *)

let liste_lignages population = List.map (function x -> lignage x population) population;;

(* Question 8 : Fonction "liste_ancetres" *)

let liste_ancetres liste_lignage = List.map(function x -> dernier x ) liste_lignage;;

(* Question 9 : Fonction "sans_double" *)
let rec sans_double_aux l table =
        match l with 
        | [] -> table
        | t::r when (List.mem t table) = false -> sans_double_aux r (t::table)
        | t::r -> sans_double_aux r table;;

let sans_double l =  
        match l with
        | [] -> l
        | _ -> sans_double_aux l [];;


(* Question 10 : Retour vers les questions *)

(* Déterminer si deux personnes p1 et p2 sont « frères de lignage » dans la population pop1. A noter que p1, p2 et pop1 ont été définies dans la question 1. *)


(* Combien de lignages avons-nous pour les populations pop1 et pop2. A noter que pop1 et pop2 ont été définies dans la question 1. *)

