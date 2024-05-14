package picture;

import java.awt.Color;

public class BubblePicture 
{
    public static void main(String[] args) 
    {
        
        Bubble bulle = new Bubble(Color.BLUE);
        Bubble bulle1 = new Bubble(Color.BLACK);
        Bubble bulle2 = new Bubble(Color.RED);
        Bubble bulle3 = new Bubble(Color.GREEN);
        while (true) 
        {
            bulle.animate();
            bulle1.animate();
            bulle2.animate();
            bulle3.animate();
        } 
    }
}