package parking;
/**
 * @inv
 */

public class Controleur {
    private FeuTricolore feu; //feu pour gérer l'état du parking
    private Barriere barriereEntre; //barrière à l'entré du parking
    private Barriere barriereSortie; //barriière à la sortie du parking 
    private Parking park; //parking 

    /**
     * 
     * @param nom1
     * @param nom2
     * @param places
     * 
     * @pre le nom des deux barrière n'est pas null et est différents, le nombre de places est supèrieur à 0
     * @post si l'utilisateur ne rentre pas de nom alors nous en métons un de base et si il ne rentre pas de 
     * place dans le parking, nous allons initialiser place à 1.
     */
    public Controleur(String nom1, String nom2, int places){
        assert nom1 != null;
        assert nom2 != null;
        assert nom1 != nom2;
        assert places > 0;  

        if(nom1 == null & nom1 == nom2){
            nom1 = "entree";
        }
        
        if(nom2 == null & nom1 == nom2){
            nom2 = "sortie";
        }

        if (places <= 0) {
            places = 1; //pas de parking à taille négtive ou égale à 0
        }

        feu = new FeuTricolore();
        barriereEntre = new Barriere(nom1);
        barriereSortie = new Barriere(nom2);
        park = new Parking(places);
    }

    /**
     * @pre le parking n'est pas plein 
     * @post park.place >= park.voiture. Si le parking est plein le feu passe au rouge (état false)
     * Quand une voiture entre la barière 1 s'ouvre et se referme après 
     */

    public void Addcar(){
        assert park.getVoiture()+1 < park.getPlaces();

        if(barriereEntre.getEtat() == false){
            barriereEntre.ouverture();
        }

        assert barriereEntre.getEtat() == true;
        
        Parking newparking = new Parking(park.getPlaces());
        newparking = park;
        newparking.addCar();

        assert newparking.getVoiture() == park.getVoiture() + 1;

        park = newparking;

        barriereEntre.ouverture();

        assert barriereEntre.getEtat() == false;

        if(park.getPlaces() == park.getVoiture() & feu.getEtat() == true){
            feu.switchState();

            assert feu.getEtat() == false;
        }
    } 

    /**
     * @pre le nombre de voiture dans le parking est superieur à 0
     * @post le nombre de voiture est superieur ou égal à 0. Si le parking était plein alors après cette fonction
     * le parking aura une place de disponible et donc changera l'état du feu à true (vert). Quand une voiture entre
     * la barière 2 s'ouvre et se referme après.
     */

    public void suppCar(){
        assert park.getVoiture()>0;

        if(barriereSortie.getEtat() == false){
            barriereSortie.ouverture();
        }

        assert barriereSortie.getEtat() == true;
        
        Parking newparking = new Parking(park.getPlaces());
        newparking = park;
        newparking.suppCar();

        assert newparking.getVoiture() == park.getVoiture()-1;
        assert newparking.getVoiture() >= 0;

        barriereSortie.ouverture();

        assert barriereSortie.getEtat() == false;

        park = newparking;

        if(feu.getEtat() == false){
            feu.switchState();

            assert feu.getEtat() == true;
        }
    }

    /**
     * 
     * @return état du feu
     */

    public boolean getFeuEtat() {
        return feu.getEtat();
    }

    /**
     * 
     * @return état parking
     */
    public boolean getParkFull() {
        return park.getPlaces() == park.getVoiture();
    }
}
