expression du besoin
- invetaire de ce que l'on souhaite
- identification du système:
	- limite externe et interne
	- le diagrame UML (le comback OMG)
	- 2e diagrame 

acteur :
entité externe qui intéragie avec le système 
c un gens qui est intéréssé, qui l'utilise, qui bénéficie du sys, qui fournis des infos 

les pricipaux acteurs sont les user du sys
un acteur correspond par un rôle
une même personne peux avoir plusieurs rôles 
si plusieurs personne possèdes les même rôle elle seront représenté par une seule personne 

relations entre cas d'utilisation
liens entre un acteur et un cas d'utilisation 
![[Pasted image 20240229082215.png]]

faut bien faire la nomenclarute vu que sinon c'est à chier.

il peux y avoir une multiplicité

![[Pasted image 20240229082849.png]]
diagramme d'un guichet bancaire 

![[Pasted image 20240229083125.png]]
la croix veux juste dire que c'est un cas particulier d'un autre rôle 

![[Pasted image 20240229083247.png]]
voilà c perlet de simplifier les trucs 

![[Pasted image 20240229084005.png]]
extend c'est un truc optionnel 
include c'est un truc obligatoire 
la croix veux dire que ca sers à rien 

![[Pasted image 20240229084207.png]]
ca hérite de tout en gros 


faut faire de la doc ... donc classico pour d'écrire tout

![[Pasted image 20240229090238.png]]
syntaxe description textuel


---
résumé de 8 slides en 1
![[Pasted image 20240301081945.png]]

![[Pasted image 20240301082545.png]]
chaque message possède une ligne de vie et un retour. Si cette dernière disparait alors ca marche plus

trace = ordre d'emission des messages 

si il y à une ligne de vie l'ordre est du haut vers le bas 
si 2 lignes de vie, ca dépends de la ligne de vie

si ils se joignent alors faut juste faire un mix and twiist de tout 

Message synchrone:
- message bloquant. Tant que l'expéditeur n'a pas de réponse du receptionneur alors il bloque. Sinon non 
- syntanxe : msg(par1,par2)
- représenté par un flèche pleine 
Message asynchrone :
- le message peu être pris en compte par le recepteur et ne renvoie pas forcément de réponse. Il n'y à pas de réponse attendu donc pas de blockage
- syntaxe : msg(par1,par2)
- flèche non pleine
Message de retour :
- c'est pour répondre suite à un message 
- syntaxe : att = msg(par1,par2) : val
- flèche en pointillés

![[Pasted image 20240301083530.png]]
classe de type signal

la fin de vie d'un objet est représenté par une croix

![[Pasted image 20240301083903.png]]
résumé de 19 slides 

message réflexif, en gros c un message qui reviens instant vers l'objet avec après un message de retour 
![[Pasted image 20240301084717.png]]


|     | opérandes | fait quoi (feur)                           |
| --- | --------- | ------------------------------------------ |
|     | alt       | alternative way                            |
|     | opt       | intéraction optionel                       |
|     | loop      | trivial                                    |
|     | break     | trivial                                    |
|     | seq       | ordre faible                               |
|     | strict    |                                            |
|     | par       | ca permet d'avoir plusieurs trace possible |
|     | critical  | doit être respecté à la lettre             |
|     | ignore    |                                            |
|     | consider  |                                            |
|     | assert    |                                            |
|     | neg       |                                            |
 
![[Pasted image 20240301091428.png]]
par

![[Pasted image 20240301092817.png]]
imposition de contraintes sur les lignes de vie de l'objet.
