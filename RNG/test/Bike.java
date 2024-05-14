package test;

public class Bike {
    private boolean avaliable;

    public Bike(boolean disponibilite){
        this.avaliable = disponibilite;
    }

    public boolean getAvaliable(){
        return this.avaliable;
    }

    public void modificationDisponibilite(){
        this.avaliable = !this.avaliable;
    }
}