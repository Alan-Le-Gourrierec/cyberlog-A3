package parking;
/**
 * @inv le nom de la barrière ne change pas. Le nom ne dois pas être null.
 */

public class Barriere {

    private final String name; //nom de la barrière qui ne dois pas être modifié
    private boolean etat; //etat de la barrière



    //constructeurs 
    /**
     * 
     * @param nom
     * @pre le nom entré n'est pas null
     * @post l'état de la barrière est fermé
     */
    public Barriere(String nom){
        assert nom != null:
            "pre contition violated : le nom est null";
        name = nom;
        etat = false; 
    }

    //methodes 

    /**
     * @post le nouvelle état est l'inverse du précédent.
     */
    public void ouverture(){
        boolean newetat = !etat;
        assert newetat != etat:
            "post condition violated : le nouvelle est le même que le précédent";
        
        if(newetat == true){
            System.out.print("la barrière est ouverte");
        } 
        else{
            System.out.print("la barrière est fermé ");
        }
    }

    //renvoie le nom de la barrière
    public String getName() {
        return name;
    }

    //renvoie l'état de la barrière
    public boolean getEtat() {
        return etat;
    }
}
