package com;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class arbreBR {
	
	public static arbre inserer(int v, arbre a){
        if(a == null) {
            return new arbre(v, null, null);
        }

		else if(v == a.getValeur()) {
			return a;
		}

		else if(v > a.getValeur()) {
			a.setFilsDroit(inserer(v, a.getFilsDroit()));
		}

		else {
			a.setFilsGauche(inserer(v, a.getFilsGauche()));
		}
		return a;
    }
    
	static void parcoursPrefixe(arbre a) {
		if(a==null){return;}

		Stack<arbre> stack = new Stack<>();
		stack.push(a);

		while(!stack.isEmpty()) {
			arbre current = stack.pop();
			System.out.print(current.getValeur() + " ");
			
			if(current.getFilsDroit() != null) {
				stack.add(current.getFilsDroit());
			}
			if(current.getFilsGauche() != null) {
				stack.add(current.getFilsGauche());
			}
		}
    }
    
    static void parcoursInfixe(arbre a) {
        if(a==null) {
            return;
        } 

        Stack<arbre> stack = new Stack<>();
        arbre current = a;        
        
        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.getFilsGauche();
            }
            current = stack.pop();
            System.out.print(current.getValeur() + " ");
            current = current.getFilsDroit();
        }
    }
    
    static void parcoursPostfixe(arbre a) {
        if(a == null) {
            return;
        }
       
        Stack<arbre> stack = new Stack<>();
        arbre current = a;
        arbre last = null;

        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.getFilsGauche();
            }
            arbre noeud = stack.peek();

            if(noeud.getFilsDroit() != null && last != noeud.getFilsDroit()) {
                current = noeud.getFilsDroit();
            }
            else {
                System.out.print(noeud.getValeur() + " ");
                last = stack.pop();
            }
        }
    }
    
    static void parcoursEnLargeur(arbre a) {
        if (a == null) {
            return;
        }
        LinkedList<arbre> list = new LinkedList<>();
        list.offer(a);

        while (!list.isEmpty()) {
            arbre current = list.poll();
            System.out.print(current.getValeur() + " ");

            if (current.getFilsGauche() != null) {
                list.offer(current.getFilsGauche());
            }
            if (current.getFilsDroit() != null) {
                list.offer(current.getFilsDroit());
            }
        }
    }
    
    static arbre supprimer(int x, arbre a) {
        if(a == null) {
            return null;
        }
        if (x == a.getValeur()) {
            return supprimerRacine(a);
        }

        if (x < a.getValeur()) {
            a.setFilsGauche(supprimer(x, a.getFilsGauche()));
        }

        else {
            a.setFilsDroit(supprimer(x, a.getFilsDroit()));
        }
        return a;
    }
    
    static arbre supprimerRacine(arbre a) {
		if (a == null) {
			return null;
		}
        arbre droit = a.getFilsDroit();

        if (droit == null) {
            return a.getFilsGauche();
        }
         
        dernierDescendant(droit).setFilsGauche(a.getFilsGauche()); 
        return droit;
    }
    
    static arbre dernierDescendant(arbre a) {
        if(a.getFilsGauche() == null) {
            return a;
        }
        else {
            return dernierDescendant(a.getFilsGauche());
        }
    }
    
    public static void main(String[] args) {
        arbre a = null;
        
        for (int i = 0; i < args.length; i++) {
            a = inserer(Integer.parseInt(args[i]), a);
        }

        System.out.println(a);
        
        System.out.print("Parcours prefixe : ");
        parcoursPrefixe(a);
        System.out.println();
        
        System.out.print("Parcours infixe :  ");
        parcoursInfixe(a);
        System.out.println();
        
        System.out.print("Parcours postfixe :  ");
        parcoursPostfixe(a);
        System.out.println();
        
        System.out.print("Parcours en largeur: ");
        parcoursEnLargeur(a);
        System.out.println();
        
        arbre a2=a;
        System.out.println("Suppression racine");
        System.out.println(supprimerRacine(a2));
        
        System.out.println("Suppression de 11");
        a=supprimer(11, a);
        System.out.println(a);
        
        System.out.println("Suppression de 3");
        
        System.out.print(supprimer(11,a));
    }     
}
