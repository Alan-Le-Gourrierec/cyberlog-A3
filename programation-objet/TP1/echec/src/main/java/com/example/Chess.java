package com.example;
import java.util.Arrays;

/**
 * A chess game. Contains a main method to play chess.
 *
 * @author Pascale Launay
 */
public class Chess
{
    /**
     * Chess playing program.
     *
     * @param args NONE
     */
    public static void main(String[] args)
    {
        // play chess
        Chess chess = new Chess();
        chess.playChess();
    }

    /**
     * Play a chess game
     */
    public void playChess()
    {
        // ask for the piece properties
        System.out.print("Give the piece name " + Arrays.asList(PieceName.values()) + ": ");
        PieceName name = PieceName.valueOf(Keyboard.readLine());
        System.out.print("Give the piece color " + Arrays.asList(PieceColor.values()) + ": ");
        PieceColor color = PieceColor.valueOf(Keyboard.readLine());

        // make a piece
        Piece piece = new Piece(name, color, 1,1);

        System.out.print(piece);
        // ask for the movement properties
        System.out.println("Give the piece movement");
        System.out.print(" dx: ");
        int dx = Keyboard.readInt();
        System.out.print(" dy: ");
        int dy = Keyboard.readInt();

        // move the piece
        piece.move(dx, dy);

        // print the piece
        System.out.println("The piece: " + piece);
    }
}
