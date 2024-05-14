package com.example;
/**
 * A chess piece. Represented by a location in the chessboard (x,y),
 * a name and a color.
 *
 * @author Pascale Launay
 */
public class Piece
{
    //attributs
    public int posx;
    public int posy;
    private final PieceName name;
    private final PieceColor color;

    //constructeur
    public Piece(PieceName name, PieceColor color, int x, int y)
    {
        this.name = name;
        this.color = color;
        this.posx = x;
        this.posy = y;
    }

    //méthode
    public PieceName getPieceName()
    {
        return this.name;
    }

    public PieceColor getPieceColor()
    {
        return this.color;
    }


    public void move(int dx, int dy)
    {   
        String nom = this.name + "";
        switch (nom) {
            case "KING":
            if(dx<=1 && dx >= -1 && dy <=1 && dy>=-1)
            {
                this.posx += dx;
                this.posy += dy;
            }
            break;

            case "QUEEN":
            if((dx == 0 && dy !=0) || (dy == 0 && dx !=0) || (Math.abs(dx) == Math.abs(dy)))
            {
                this.posx += dx;
                this.posy += dy;
            }
            break;

            case "BISHOP":
            if(Math.abs(dx) == Math.abs(dy))
            {
               this.posx += dx;
               this.posy += dy; 
            }
            break;

            case "KNIGHT":
            if((Math.abs(dx) == 2 && Math.abs(dy) == 1) || (Math.abs(dx) == 1 && Math.abs(dy) == 2))
            {
                
            }
            break;

            case "ROOK":
            if((dy == 0 && dx !=0) || (dy !=0 && dx ==0))
            {
                this.posx += dx;
                this.posy += dy;
            }
            break;

            case "PAWN" :
            if(dx ==0 && dy ==1)
            {
                this.posy += dy;
            }
            break;

            default :
            System.out.println("ERROR, invalid values");
            break;
        }
        
    }

    @Override
    public String toString()
    {
        return this.name + " " + this.color + " posx : " + this.posx + " posy : " + this.posy ;
    }
}
