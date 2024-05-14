package pile;

public class Liste {
    //attributs
    private int contenu;
    private Liste suivant;

    //constructeur
    public Liste(int val, Liste st){
        this.contenu = val;
        this.suivant = st;
    }

    //methode
    public int getContenu() {
        return contenu;
    }
    public Liste getSuivant() {
        return suivant;
    }
}
