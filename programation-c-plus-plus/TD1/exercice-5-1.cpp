#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<double> Table;
    cout << "Entrez des valeurs, et lorsque vous souhaitez arrêter, entrez 0 :" << endl;
    double var = 1;
    double sum = 0;

    while (var != 0) {
        cin >> var;
        sum += var;
        Table.push_back(var);
    }

    // Affichage de la somme
    cout << "La somme de tous les nombres est : " << sum << endl;

    // Affichage des valeurs dans l'ordre d'entrée
    cout << "Les valeurs entrées dans l'ordre sont : ";
    for (int i = 0; i < Table.size(); ++i) {
        cout << Table[i] << "  ";
    }

    // Tri du vecteur
    sort(Table.begin(), Table.end());

    // Affichage des valeurs triées
    cout << "\nLes valeurs triées sont : ";
    for (int i = 0; i < Table.size(); ++i) {
        cout << Table[i] << "  ";
    }

    return 0;
}