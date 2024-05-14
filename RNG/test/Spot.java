package test;

public class Spot{

    private final Location location;
    private final boolean electric;
    private Bike velo;

    public Spot(Location location, boolean electric)
    {
        this.location = location;
        this.electric = electric;
    }
    public Location getLocation()
    {
        return this.location;
    }
    public boolean isElectric()
    {
        return this.electric;
    }

    public Bike Fixer(Bike bike){
        bike.modificationDisponibilite();
        this.velo = bike;
        return this.velo;
    }

    public Bike retirer(){
        Bike bike = this.velo;
        bike.modificationDisponibilite();
        this.velo = null;
        return bike;
    }

    public Bike getVelo() {
        return velo;
    }

}
