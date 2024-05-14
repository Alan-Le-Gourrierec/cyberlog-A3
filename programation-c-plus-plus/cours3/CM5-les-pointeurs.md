## Les fonctions

les blocs de fonctions c classico, 

## pointeurs 

```cpp
#include <iostream>

using namespace std;

int main()
{
int entier = 42; //entier classico pour les test
int* pointeur = &entier; //pointeur enregistre l'emplacement de la variable
int valeur = *pointeur; //poite la valeur dans le pointer (donc 42)

cout<<"entier : "<<entier<<"\n"<<"pointeur : "<<pointeur<<endl;
cout<<"valeur : "<<valeur;
return 0;
}
```

cf (exemple code swap)[[programation-c-plus-plus/cours3/exercice2-pointeur.cpp]]

## allocation de mémoire 

```cpp
#include <iostream>

int main() {
    // Allocation dynamique d'un entier
    int* entierDynamique = new int;

    // Attribution d'une valeur à l'entier alloué dynamiquement
    *entierDynamique = 42;

    // Affichage de la valeur
    std::cout << "Valeur de l'entier dynamique : " << *entierDynamique << std::endl;

    // Libération de la mémoire allouée dynamiquement
    delete entierDynamique;

    // Allocation dynamique d'un tableau d'entiers
    int* tableauDynamique = new int[5];

    // Attribution de valeurs au tableau
    for (int i = 0; i < 5; ++i) {
        tableauDynamique[i] = i * 10;
    }

    // Affichage des valeurs du tableau
    std::cout << "Valeurs du tableau dynamique : ";
    for (int i = 0; i < 5; ++i) {
        std::cout << tableauDynamique[i] << " ";
    }
    std::cout << std::endl;

    // Libération de la mémoire allouée dynamiquement pour le tableau
    delete[] tableauDynamique;

    return 0;
}
```

