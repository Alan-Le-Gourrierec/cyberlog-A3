package com.example;

public class jeuTheKiller {
    public static void main(String[] args) {
        Tueur joseph = new Tueur("joseph"); //1er tueur 
        Tueur ewan = new Tueur("ewan"); // 2e tueur
        Tueur MaximeL = new Tueur("maxime L", joseph); //3e tueur

        joseph.setContract(ewan);
        ewan.setContract(MaximeL);

        ListeTueurs T1 = new ListeTueurs(joseph);
        System.out.println(T1.getNombre());
        T1.affichage();
        T1.insert("Maxime S");
        T1.insert("Margaux");
        T1.affichage();

        ListeTueurs T2 = new ListeTueurs();
        T2.insert("Batiste");
        T2.insert("Alan");
        T2.insert("Anthony");
        T2.affichage();

        T1.insererListe(T2);
        T1.affichage();
    }
}
