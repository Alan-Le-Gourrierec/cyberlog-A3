package picture;

import java.awt.Color;

public class Sun extends Circle {
    private static final Color color = Color.YELLOW;
    Circle soleil;

    public Sun(int x, int y, int size)
    {
        super(x, y, size,color);
    }

    public void animate(int iterations)
    {
        for(int i = 0; i<iterations; i++)
        {
            move();
            CanvasFrame.getCanvas().redraw();
            CanvasFrame.getCanvas().wait(20);
            if(i>=600)
            {
                break;
            }
        }
    }
}
