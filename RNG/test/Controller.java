package test;

import java.util.List;
public class Controller
    {
    private final List<Spot> spots;
    public Controller(List<Spot> spots)
    {
         this.spots = spots;
    }

    /**
     * @pre l'autonomie du vélo dois petre supèrieur à 50 et elle ne peux pas être infèrieur à 0 ou suppèrieur à 100
     */
    public Spot getSpot(Location location, boolean hasBike, boolean electric)
    {
        double d = 123456789;
        Spot best = null;
        for(Spot i : spots){
            if(i.isElectric() != electric & i.getVelo() != null){
                break;
            }
            double tmp = location.distance(i.getLocation());
            if(tmp < d){
                d = tmp;
                best = i;
            }
        }
        return best;
    }
}