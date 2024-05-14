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
