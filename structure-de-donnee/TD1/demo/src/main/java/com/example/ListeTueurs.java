package com.example;

public class ListeTueurs {
    private Tueur[] tete;
    private int nombre;

    ListeTueurs() {
        this.tete = null;
        this.nombre = 0;
    }

    ListeTueurs(Tueur T) {
        this.nombre = 1;
        Tueur Temp = T;
        while (T != Temp.getContrat()) {
            Temp = Temp.getContrat();
            this.nombre += 1;
        }

        tete = new Tueur[nombre];
        for (int i = 0; i < nombre; i++) {
            tete[i] = T;
            T = T.getContrat();
        }
    }

    private void majList(Tueur T) {
        this.nombre = 1;
        Tueur Temp = T;
        while (T != Temp.getContrat()) {
            Temp = Temp.getContrat();
            this.nombre += 1;
        }
    
        Tueur[] newTete = new Tueur[nombre];
        for (int i = 0; i < nombre; i++) {
            newTete[i] = T;
            T = T.getContrat();
        }
        this.tete = newTete;
    }

    public int getNombre() {
        return nombre;
    }

    //methodes
    void affichage() {
        if (this.tete == null) {
            System.out.print("Warning (affichage) : la liste est vide !");
        } 
        else {
            for (int i = 0; i < nombre-1; i++) {
                System.out.print(tete[i].getNom() + " --> ");
            }
            System.out.print(tete[nombre - 1].getNom() + "\n");
        }
    }

    void insert(String name) {
        Tueur T = new Tueur(name);
        if (this.tete == null) {
            T.setContract(T);
            majList(T);
        } else {
            int pos = (int) Math.floor((Math.random() * (nombre - 1)));
            T.setContract(tete[pos]);
            if (pos == 0) {
                tete[nombre - 1].setContract(T);
                majList(T);
            } else {
                tete[pos - 1].setContract(T);
                majList(tete[0]);
            }
        }
    }

    void insererListe(ListeTueurs T){
        for(int i = 0; i<T.nombre; i++){
            this.insert(T.tete[i].getNom());
        }
    }
}
