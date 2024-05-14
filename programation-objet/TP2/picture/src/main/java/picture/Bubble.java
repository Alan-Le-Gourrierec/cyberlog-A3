package picture;

import java.awt.Color;
import java.util.Random;

public class Bubble extends Circle
{
    public static final double pi = 3.1415927;
    private static final int size = 30;
    private static final double alpha = pi/2;
    private static final int dist = 2;
    private int directionx = 1;
    private int directiony = 1;

    Circle bulle;

    public Bubble(Color color)
    {
        super(randomInt(500),randomInt(500),size,color);
    }
    private static int randomInt(int borne)
    {
        Random random = new Random();
        return random.nextInt(borne);
    }

    private double random(double borne)
    {
        Random random = new Random();
        return - borne + 2 * borne * random.nextDouble();
    }

    private void direction()
    {
        if(this.directionx == -1 && this.getX()<20){this.directionx = 1;} 
        if(this.directionx == 1 && this.getX()>480){this.directionx = -1;} 
        if(this.directiony == -1 && this.getY()<20){this.directiony = 1;} 
        if(this.directiony == 1 && this.getY()>480){this.directiony = -1;} 
    }

    @Override
    public synchronized void move() {
        direction();
        int x = (int) Math.round(this.directionx * Math.cos(alpha + random(pi/6)) * dist + this.getX()/1000);
        int y = (int) Math.round(this.directiony * Math.sin(alpha - random(pi/6)) * dist + this.getY()/1000);
        super.move(x, y);
    } 

    public void animate()
    {
        move();
        CanvasFrame.getCanvas().redraw();
        CanvasFrame.getCanvas().wait(20);
    }
}