l'héritage,
blablabla
```java
// Classe de base (classe mère)
class Animal {
    private String nom;

    public Animal(String nom) {
        this.nom = nom;
    }

    public void parler() {
        System.out.println("La méthode parler doit être implémentée dans les classes dérivées.");
    }
}

// Classe dérivée (classe fille)
class Chien extends Animal {
    public Chien(String nom) {
        super(nom);
    }

    @Override
    public void parler() {
        System.out.println(this.getNom() + " dit Woof !");
    }
}

// Classe dérivée (classe fille)
class Chat extends Animal {
    public Chat(String nom) {
        super(nom);
    }

    @Override
    public void parler() {
        System.out.println(this.getNom() + " dit Meow !");
    }
}

// Classe principale
public class Main {
    public static void main(String[] args) {
        Chien chien1 = new Chien("Buddy");
        Chat chat1 = new Chat("Whiskers");

        chien1.parler();  // Affiche "Buddy dit Woof !"
        chat1.parler();   // Affiche "Whiskers dit Meow !"
    }
}
```

Si une méthode est défini comme un clochard, càd tu nomme bien => tu overwrite pas ta méthode. Mais stv la grand remplacer ca prends la plus haute dans le hierarchies sinon.

```java
class Calculateur {
    public int additionner(int a, int b) {
        return a + b;
    }

    public double additionner(double a, double b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculateur calculateur = new Calculateur();

        int resultatEntier = calculateur.additionner(5, 10);
        double resultatDouble = calculateur.additionner(5.5, 10.5);

        System.out.println("Résultat entier : " + resultatEntier);  // Affiche "Résultat entier : 15"
        System.out.println("Résultat double : " + resultatDouble);  // Affiche "Résultat double : 16.0"
    }
}

```

## Overwrite
méthode pour deux class (héréditaire) différente avec un même nom

```java
// Classe de base
class Forme {
    public void dessiner() {
        System.out.println("Dessin d'une forme générique");
    }
}

// Classe dérivée
class Cercle extends Forme {
    @Override
    public void dessiner() {
        System.out.println("Dessin d'un cercle");
    }
}

// Classe dérivée
class Carre extends Forme {
    @Override
    public void dessiner() {
        System.out.println("Dessin d'un carré");
    }
}

// Classe principale
public class Main {
    public static void main(String[] args) {
        Forme forme1 = new Cercle();
        Forme forme2 = new Carre();

        forme1.dessiner();  // Affiche "Dessin d'un cercle"
        forme2.dessiner();  // Affiche "Dessin d'un carré"
    }
}

```

## surcharge

en gros methode mais avec un nbr de paramètre d'entré différent 

```java
class Calculatrice {

    // Méthode pour additionner deux entiers
    public int additionner(int a, int b) {
        System.out.println("Méthode pour additionner deux entiers");
        return a + b;
    }

    // Surcharge : Méthode pour additionner trois entiers
    public int additionner(int a, int b, int c) {
        System.out.println("Surcharge : Méthode pour additionner trois entiers");
        return a + b + c;
    }

    // Surcharge : Méthode pour additionner deux doubles
    public double additionner(double a, double b) {
        System.out.println("Surcharge : Méthode pour additionner deux doubles");
        return a + b;
    }

    // Surcharge : Méthode pour concaténer deux chaînes de caractères
    public String additionner(String a, String b) {
        System.out.println("Surcharge : Méthode pour concaténer deux chaînes de caractères");
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculatrice calculatrice = new Calculatrice();

        // Utilisation des différentes méthodes
        System.out.println(calculatrice.additionner(5, 10));                    // Affiche "Méthode pour additionner deux entiers"
        System.out.println(calculatrice.additionner(5, 10, 15));                // Affiche "Surcharge : Méthode pour additionner trois entiers"
        System.out.println(calculatrice.additionner(5.5, 10.5));                // Affiche "Surcharge : Méthode pour additionner deux doubles"
        System.out.println(calculatrice.additionner("Hello", "World"));        // Affiche "Surcharge : Méthode pour concaténer deux chaînes de caractères"
    }
}

```

## abstract 
en gros tu peux pas l'utiliser comme ca et après tu fait une final et tu peux plus la réutiliser 
```java
// Classe abstraite
abstract class Forme {
    private String couleur;

    // Constructeur
    public Forme(String couleur) {
        this.couleur = couleur;
    }

    // Méthode concrète
    public void afficherCouleur() {
        System.out.println("La couleur de la forme est : " + couleur);
    }

    // Méthode abstraite
    abstract double calculerSurface();
}

// Classe dérivée
class Cercle extends Forme {
    private double rayon;

    // Constructeur
    public Cercle(String couleur, double rayon) {
        super(couleur);
        this.rayon = rayon;
    }

    // Implémentation de la méthode abstraite
    @Override
    double calculerSurface() {
        return Math.PI * rayon * rayon;
    }
}

// Classe dérivée
class Carre extends Forme {
    private double côté;

    // Constructeur
    public Carre(String couleur, double côté) {
        super(couleur);
        this.côté = côté;
    }

    // Implémentation de la méthode abstraite
    @Override
    double calculerSurface() {
        return côté * côté;
    }
}

// Classe principale
public class Main {
    public static void main(String[] args) {
        Cercle cercle = new Cercle("Rouge", 5.0);
        Carre carre = new Carre("Bleu", 4.0);

        cercle.afficherCouleur();
        System.out.println("Surface du cercle : " + cercle.calculerSurface());

        carre.afficherCouleur();
        System.out.println("Surface du carré : " + carre.calculerSurface());
    }
}

```

## Interface 
en gros c un absctract sans builder

```java
// Interface
interface Forme {
    // Méthode abstraite (sans implémentation)
    double calculerSurface();

    // Méthode abstraite (sans implémentation)
    void afficherCouleur();
}

// Classe implémentant l'interface
class Cercle implements Forme {
    private String couleur;
    private double rayon;

    // Constructeur
    public Cercle(String couleur, double rayon) {
        this.couleur = couleur;
        this.rayon = rayon;
    }

    // Implémentation de la méthode de l'interface
    @Override
    public double calculerSurface() {
        return Math.PI * rayon * rayon;
    }

    // Implémentation de la méthode de l'interface
    @Override
    public void afficherCouleur() {
        System.out.println("La couleur du cercle est : " + couleur);
    }
}

// Classe principale
public class Main {
    public static void main(String[] args) {
        Cercle cercle = new Cercle("Rouge", 5.0);

        // Utilisation des méthodes de l'interface
        cercle.afficherCouleur();
        System.out.println("Surface du cercle : " + cercle.calculerSurface());
    }
}
```
