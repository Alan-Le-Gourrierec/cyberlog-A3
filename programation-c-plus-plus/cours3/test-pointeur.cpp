#include <iostream>

using namespace std;

int main()
{
    int entier = 42;
    int* pointeur = &entier;
    int valeur = *pointeur;

    cout<<"entier : "<<entier<<"\n"<<"pointeur : "<<pointeur<<endl; 
    cout<<"valeur : "<<valeur;
    
    return 0;
}