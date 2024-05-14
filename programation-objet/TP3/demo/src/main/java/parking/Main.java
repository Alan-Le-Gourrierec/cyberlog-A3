package parking;

import java.util.Scanner;

public class Main {
    /**
     * ce programme est le main. Il réalise la création d'un parking
     * @action nous pouvons ajouter et enlever des voitures 
     * @param args utilisé pour les scanners (scanners pour initialiser notre controleur (représentant le parking)
     * scannerOption utilisé pour le switchcase pour ajouter, retirer ou encore quiter le programme)
     */
    public static void main(String[] args) {
        /*
         * initialisation de notre parking. Le programme à été bien fait nous prenons en compte les potentiels problèmes 
         * grâce à la programmation défensive réalisé. Il n'y à donc normalement pas d'issue et donc le programme prévois
         * les divers problème pouvant être lié.
         */
        Scanner scanner = new Scanner(System.in);
        System.out.print("entrer la taille du parking");

        int size = scanner.nextInt();
        
        System.out.println("entrer les noms de vos barières (nom1 puis nom2)");
        
        String nom1 = scanner.nextLine();
        String nom2 = scanner.nextLine();

        scanner.close();

        Controleur parking = new Controleur(nom1, nom2, size);
        String option = "";

        System.out.println("pour ajouter une voiture faites '+' \n pour enlever une voiture faites '-'\n pour quiter faites n'importe quelle touche");

        while (true) {
            Scanner scannerOption = new Scanner(System.in);
            option = scannerOption.nextLine();
            switch (option) {
                case "+":
                    parking.Addcar();
                    break;
                case "-":
                    parking.suppCar();
                    break;
            
                default:
                    scannerOption.close();
                    System.exit(0); // quitter le priogramme
            }
        }   


    }    
}
