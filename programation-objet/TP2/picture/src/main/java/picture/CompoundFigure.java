package picture;

import java.awt.Canvas;
import java.awt.Color;

public abstract class CompoundFigure extends Figure{
    //attribut
    private Figure[] TableauFigure;

    public CompoundFigure(int x, int y,Figure[] Table)
    {
        super(x, y);
        this.TableauFigure = Table;
        
    }

    public void draw()
    {
        int size = this.TableauFigure.length;
        for(int i = 0; i<size; i++)
        {
            CanvasFrame.getCanvas().draw(this.TableauFigure[i]);
        }
        CanvasFrame.getCanvas().redraw();
    }

    public void erase()
    {
        int size = this.TableauFigure.length;
        for(int i = 0; i<size; i++)
        {
            CanvasFrame.getCanvas().erase(this.TableauFigure[i]);
        }
        CanvasFrame.getCanvas().redraw();
    }
}