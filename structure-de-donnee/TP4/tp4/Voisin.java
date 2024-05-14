package tp4;

/**
 * Voisin
 */
public class Voisin {
    private Paire<String, Integer>[] voisin;

    Voisin(Paire[] voisin) {
        this.voisin = voisin;
    }

    Voisin(Paire[] voisin, int poids, String sommet) {
        int len = voisin.length;
        this.voisin = new Paire[len +1];

        for(int i = 0; i < len; i++) {
            this.voisin[i] = voisin[i];
        }

        this.voisin[len+1] = new Paire<String,Integer>(sommet, poids);
    }

    public void AddVoisin(String sommet, int poids) {
        Voisin nouveau = new Voisin(this.voisin, poids, sommet);
        this.voisin = nouveau.getVoisin();
    }

    public Paire<String, Integer>[] getVoisin() {
        return voisin;
    }
}