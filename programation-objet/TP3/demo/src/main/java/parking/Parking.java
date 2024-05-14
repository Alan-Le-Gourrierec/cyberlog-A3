package parking;
/**
 * @inv voiture <= places and place > 0 and voiture >= 0
 */
public class Parking {
    private int places; //nombre de place dans le parking
    private int voiture; //nombre de voiture

    /**
     * @param nombreplace
     * @pre  le nombre de places dois être supèrieur à 0.
     * @post le nombre de places dans le parking est le même que celui entrél et le parking est vide
     */

    Parking(int nombreplace){
        assert nombreplace > 0:
            "pre condition violated ; le nombre de place dans le parking initialisé est infèrieur ou égal à 0";
        places = nombreplace;
        voiture = 0;
        assert places == nombreplace:
            "post condition violated : le nombre de places de parking entré et celui dans le paking ne sont pas les mêmes";
        assert places > 0:
            "pre condition violated ; le nombre de place dans le parking est infèrieur à 0";
        assert voiture >=0 & voiture > nombreplace; 
    }

    //methode
    /**
     * @pre le nombre de voiture est supèrieur ou égal à 0
     * @post le nombre de voiture dans le parking est incrémenté de 1 et le nombre de voiture dans 
     *       le parking est infèrieur ou égal au nombrd de places
     */
    public void addCar(){
        assert voiture >=0;
        int temp = voiture++;
        assert temp == voiture++;
        assert temp > places;
        voiture = temp;
    }

    /**
     * @pre le nombre de voiture est supèrieur à 0
     * @post le nombre de voiture est supèrieur ou égal à 0 et le nombre de voiture à réduit de 1
     */
    public void suppCar(){
        assert voiture >0;
        int temp = voiture--;
        assert temp == voiture--;
        assert temp>0;
        voiture = temp; 
    }

    /**
     * @post ne modifie pas la valuer de places
     * @return la valeur de places
     */
    public int getPlaces() {
        return places;
    }

    /**
     * @post ne modifie pas la valeur de voiture
     * @return
     */
    public int getVoiture() {
        return voiture;
    }
}
