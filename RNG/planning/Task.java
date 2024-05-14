package planning;
import java.util.Date;

public class Task {
    Date startDate;
    Date endDate;
    String title;
    String description;

    Task(Date debut, Date fin, String titre, String description){
        this.startDate = debut;
        this.endDate = fin;
        this.title = titre;
        this.description = description;
    }

    public Date getStartDate() {
        return startDate;
    }

    public Date getEndDate() {
        return endDate;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }
}