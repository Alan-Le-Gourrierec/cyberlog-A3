#include <iostream>

using namespace std;

void initVar(int &a, const int b, int* c, int &d, const int &e, int g = 6)
{
    a = 1;
    // b = 2;  // La variable 'b' est constante, elle ne peut pas être modifiée ici
    *c = 3;
    d = 4;
    // e = 5;  // La variable 'e' est constante, elle ne peut pas être modifiée ici
    cout << "g=" << g << endl;
}

int main()
{
    int a = 0;  // Initialisez les variables a, b, c, d, e, g avec des valeurs initiales
    int b = 0;
    int c = 0;
    int d = 0;
    int e = 0;
    int g = 0;

    initVar(a, b, &c, d, e, g);
    cout << "a=" << a << ", b=" << b << ", c=" << c << ", d=" << d << ", e=" << e << ", g=" << g << endl;

    initVar(a, b, &c, d, e, g);
    cout << "a=" << a << ", b=" << b << ", c=" << c << ", d=" << d << ", e=" << e << ", g=" << g << endl;

    return 0;
}

