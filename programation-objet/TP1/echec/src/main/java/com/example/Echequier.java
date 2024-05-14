package com.example;

public class Echequier {

    //attributs
    Piece[][] chess;

    //constructeur
    Echequier() {
        this.chess = new Piece[8][8];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++)
            {
                this.chess[i][j] = null;
            }
        }
    }

    //methode
    Echequier Deplacer(Echequier plateau, Piece pion) 
    {
        plateau.chess[pion.posx][pion.posy] = pion;
        return plateau;
    }
    
    void ShowPiece(Echequier plateau, int posx, int posy)
    {
        System.out.print(plateau.chess[posx][posy].getPieceName());
        System.out.print(" ");
        System.out.print(plateau.chess[posx][posy].getPieceColor());
    }

    void ShowEchec(Echequier plateau)
    {
        for(int i = 0; i < 8; i++)
        {
            for(int j = 0; j < 8; j++)
            {
                ShowPiece(plateau, i, j);
                System.out.print(" | ");
            }
            System.out.println("");
        }
    }

    int LeftPieceColor(PieceColor color, Echequier plateau)
    {
        int count = 0;
        for(int i = 0; i < 8; i++)
        {
            for(int j = 0; j < 8; j++)
            {
                if(plateau.chess[i][j].getPieceColor() ==color){count++;}
            }
        }
        return count;
    }

    Piece FoundPiece(PieceColor color, PieceName name, Echequier plateau)
    {
        for(int i = 0; i<8; i++)
        {
            for(int j = 0; j<8;j++)
            {
                if(plateau.chess[i][j].getPieceColor()==color && plateau.chess[i][j].getPieceName()==name)
                {
                    return plateau.chess[i][j];
                }
            }
        }
        return null;
    }

    Echequier RemovePiece(Echequier plateau, PieceColor color, PieceName name)
    {
        Piece pion = FoundPiece(color, name, plateau);
        plateau.chess[pion.posx][pion.posy] = null;
        return plateau;
    }

    Echequier ChecMove(Piece pion, int dx, int dy, Echequier plateau)
    {
        if(pion.posx+dx < 8 && pion.posx+dx>=0 && pion.posy+dy <8 && pion.posy>=0)
        {
            plateau = Deplacer(plateau, pion);
        }
        return plateau;
    }
}


