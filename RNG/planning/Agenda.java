package planning;
import java.util.Date;
/**
 * An agenda composed of tasks
    */
 public class Agenda {
    
    Task[] taches;
    /** The tasks list declaration */
    // TODO
    
    /**
    * Initialize the tasks list
    */
    public Agenda() {
        this.taches = new Task[0];
    }
    
    /**
    * Add a task in the tasks list
    *
    1 @param task the new task
    */
    public void addTask(Task task) {
        int size = this.taches.length;
        Task[] tmp = new Task[size+1];
        
        for(int i = 0; i < size; i++){
            tmp[i] = this.taches[i];
        }

        tmp[size + 1] = task;
        this.taches = tmp;
    }
    /**
     * 
     * @param d1 date réprésentant la borne infèrieur 
     * @param d2 date représentant la borne supèrieur
     * @return
     * @pre d1<d2
     */

    public Task[] between(Date d1, Date d2){
        Agenda solve = new Agenda();
        for(int i = 0; i < this.taches.length; i++){
            if(this.taches[i].getStartDate().compareTo(d1) <= 0 & this.taches[i].getStartDate().compareTo(d1)>= 0){
                solve.addTask(this.taches[i]);
            }
        }
        return solve.taches;
    }
}