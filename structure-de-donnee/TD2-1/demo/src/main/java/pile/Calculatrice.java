package pile;

public class Calculatrice {
    //attributs
    private Pile calculatrice;

    //constructeur
    Calculatrice(Pile p){
        calculatrice = p;
    }
    Calculatrice(){
        calculatrice = new Pile();
    }

    //methode
    public void funADD(){
        calculatrice.empiler(calculatrice.depiler()+calculatrice.depiler());
    }

    public void funSUB(){
        calculatrice.empiler(calculatrice.depiler()-calculatrice.depiler());
    }

    public void  funMUL(){
        calculatrice.empiler(calculatrice.depiler()*calculatrice.depiler());
    }

    public void funDIV(){
        int dividand = calculatrice.depiler();
        int diviseur = calculatrice.depiler();
        if(diviseur != 0){
            calculatrice.empiler((int) Math.floor(dividand / diviseur));
        }
        else{
            System.out.print("division par 0.");
        }
    }
    
    public void funDSP(){
        calculatrice.afficherPile();
    }

    public static void main(String[] args) {
        Calculatrice stack = new Calculatrice();
        int size = args.length;
        for(int i = 0; i< size; i++)
            try{
                stack.calculatrice.empiler((Integer.parseInt(args[i])));
            }
            catch(NumberFormatException e){
                switch (args[i]) {
                    case "ADD":
                        stack.funADD();
                        break;
                    case "SUB":
                        stack.funSUB();
                        break;
                    case "MUL":
                        stack.funMUL();
                        break;
                    case "DIV":
                        stack.funDIV();
                        break;
                    case "DSP":
                        stack.funDSP();
                    default:
                        break; 
            }
        }
        stack.funDSP();
    }
}
