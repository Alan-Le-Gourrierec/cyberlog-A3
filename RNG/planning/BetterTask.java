package planning;

import java.util.Date;

public class BetterTask extends Task{
    private int repetition;
    private int jour;

    BetterTask(Date debut, Date fin, String titre, String description, int repeat, int days){
        super(debut, fin, titre, description);
        this.repetition = repeat;
        this.jour = days;
    }

    public int getJour() {
        return jour;
    }

    public int getRepetition() {
        return repetition;
    } 
}
