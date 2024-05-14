package parking;

/** @inv etat = true or etat = false */
public class FeuTricolore {
    //
    private boolean etat;

    /**
     * @pre le feu à été initialisé et nous ne gérons que 2 état : rouge ou vert
     * @post le feu est de l'inverse de la couleur d'avant et reste rouge ou vert de
     *       plus nous informons du changement
     */

    // constructeurs
    public FeuTricolore(boolean statu) {
        etat = statu;
    }

    public FeuTricolore() {
        etat = false;
    }

    // methode
    //permet d'inverser l'état du feu précédent, de plus ceci sera notifié 
    public void switchState() {
        boolean newetat = !etat;
        assert newetat != this.etat:
            "Post condition violated : l'état précédent est le même que l'ancien";
        if(newetat == true){
            System.out.print("le feu est au vert");
        }
        else{
            System.out.print("le feu est au rouge");
        }
        this.etat = newetat;
    }
    
    //renvoir l'état à l'instant t de la barrière
    public boolean getEtat() {
        return etat;
    }
    

}