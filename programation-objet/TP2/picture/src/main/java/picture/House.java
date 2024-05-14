package picture;

import java.awt.Color;
import java.awt.Graphics2D;

public class House extends CompoundFigure {

    public House(int x, int y, int width, int height) {
        super(x, y, buildHouseFigures(x, y, width, height));
    }

    private static Figure[] buildHouseFigures(int x, int y,int width, int height) {
        Figure[] houseFigures = new Figure[4];

        // Create wall
        Figure wall = new Rectangle(x, y, width, height, Color.BLACK);
        houseFigures[0] = wall;

        // Create rooff
        Figure roof = new Triangle(x, y- Math.abs(height/2) , width, Math.abs(height/2), Color.RED);
        houseFigures[1] = roof;

        // Create door
        Figure door = new Rectangle(x + width - Math.abs(width/3)  , y + height - 2 - Math.abs(height/2), Math.abs(width/5), Math.abs(height/2), Color.WHITE);
        houseFigures[2] = door;

        // Create window
        Figure window = new Square(x + Math.abs(width/10) , y + Math.abs(height/3), Math.abs(height/3), Color.WHITE);
        houseFigures[3] = window;

        return houseFigures;
    }

    @Override
    public void draw() {
        super.draw();
        // Additional drawing logic specific to House, if needed
    }

    @Override
    public void erase() {
        super.erase();
        // Additional erasing logic specific to House, if needed
    }

    @Override
    protected void draw(Graphics2D graphics) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'draw'");
    }

    @Override
    public int getWidth() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getWidth'");
    }

    @Override
    public int getHeight() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getHeight'");
    }
}


