package pile;

public class Pile {
    //attributs
    private Liste sommet;

    //constructeurs
    public Pile(Liste st){
        this.sommet = st;
    }

    public Pile(){
        this.sommet = null;
    }

    //methode
    public boolean estVide(){
        return sommet == null;
    }
    public void empiler(int element){
        sommet = new Liste(element,sommet);
    }

    public int depiler(){
        if(estVide() != false){
            int tmp = sommet.getContenu();
            sommet = sommet.getSuivant();
            return tmp;
        }
        else{
            System.err.println("il n'y à pas d'autre valeurs");
            return -1;
        }
    }

    public void afficherPile(){
        Liste tmp = sommet;
        System.out.print("| ");
        while (tmp.getSuivant() != null) {
            System.out.print(tmp.getContenu() + " | ");
            tmp = tmp.getSuivant();
        } 
    } 
    
}
