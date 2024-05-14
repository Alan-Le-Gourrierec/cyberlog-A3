package com.example;

public class Tueur {

    private String nom;
    private Tueur contrat;

    public Tueur(String name){
        this.nom = name;
        this.contrat = null;
    }

    public Tueur(String name, Tueur killer){
        this.nom = name;
        this.contrat = killer;
    }

    void setContract(Tueur T)
    {
        this.contrat=T;
    }
    
    public String getNom() {
        return nom;
    }
    
    public Tueur getContrat() {
        return contrat;
    }
}