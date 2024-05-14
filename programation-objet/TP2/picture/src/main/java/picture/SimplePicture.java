package picture;

import java.awt.Color;

public class SimplePicture 
{
    private Circle cercle;
    private Person george;
    private House maison;
    private Sun soleil;

    public SimplePicture( Circle cercle, Person person, House house, Sun sun)
    {
        this.cercle = cercle;
        this.george = person;
        this.maison = house;
        this.soleil = sun;
    }

    public void draw()
    {
       this.cercle.makeShape();
       this.george.makeShape();
       CanvasFrame.getCanvas().draw(george);
       CanvasFrame.getCanvas().draw(cercle);
       maison.draw();
       soleil.draw();
       CanvasFrame.getCanvas().redraw();
    }
    /* 
    public static void main(String[] args) {
        Person alan;
        Circle cercle;
        SimplePicture picture;
        House maison;
        Sun soleil;

        maison = new House(250, 250,120,100);
        alan = new Person(100, 100, 100, 100, Color.BLACK);
        cercle = new Circle(200, 200, 200, Color.GREEN);
        soleil = new Sun(0,50,100);

        picture = new SimplePicture(cercle, alan, maison, soleil);
        picture.draw();
        soleil.animate(1000);
    }*/
}
