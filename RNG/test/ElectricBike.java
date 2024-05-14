package test;

/**
 * @inv la valeur de la autonomie est constante 
 */
public class ElectricBike extends Bike{
    private int autonomie;

    ElectricBike(boolean disponibilite, int batterie){
        super(disponibilite);
        this.autonomie = batterie;
    }

    public int getAutonomie() {
        return autonomie;
    }
}
