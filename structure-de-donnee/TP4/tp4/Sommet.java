package tp4;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Sommet {
    private String etiquet;
    private Voisin voisin;

    public Sommet(String tag) {
        this.etiquet = tag;
    } 
   
    public Boolean estVoisin(Sommet sommet) {
        Paire<String, Integer>[] neighbor = this.voisin.getVoisin();
        for(int i = 0; i < neighbor.length; i++) {
            if (sommet.getEtiquet().equals(neighbor[i].getFirst())) {
                return true;
            }
        }
        return false;
    }

    public void ajouterVoisin(Sommet sommet, int poids) {
        Paire<String, Integer>[] neighbor = this.voisin.getVoisin();
        if (!estVoisin(sommet)) {
            this.voisin = new Voisin(neighbor, poids, etiquet);
        }
    }

    public Iterator<Paire<String, Integer>> voisins() {
        Set<String> voisinUnique = new HashSet<>();
        Set<Paire<String,Integer>> voisinsSet = new HashSet<>();
        Iterator<Paire<String, Integer>> iterator = voisin.voisins();

        while (iterator.hasNext()) {
            Paire<String, Integer> neighbor = iterator.next();
            if (!voisinUnique.contains(neighbor.getFirst())) {
                voisinsSet.add(neighbor);
                voisinUnique.add(neighbor.getFirst());
            }
        }
        return voisinsSet.iterator();
    }

    public String getEtiquet() {
        return etiquet;
    }
}
