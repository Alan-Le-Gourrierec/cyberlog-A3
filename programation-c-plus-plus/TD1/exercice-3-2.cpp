#include <iostream>
#include <iomanip>
#include <limits>
#include <cmath>

int main() {
    long double pi = 3.14159265358979323846264338327950288419716939937510582L;

    // Obtenir la précision maximale pour le type long double
    int max_precision = std::numeric_limits<long double>::digits10;

    // Affichage avec la précision maximale
    std::cout << "valeur aproximative de pi : " << std::setprecision(max_precision) << pi << std::endl;

    return 0;
}
