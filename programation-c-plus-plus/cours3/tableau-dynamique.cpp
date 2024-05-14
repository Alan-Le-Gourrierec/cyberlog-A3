#include <iostream>

using namespace std;

class Noeud
{
public:
    int data;
    Noeud *suivant;

    Noeud(int valeur) : data(valeur), suivant(nullptr) {}
};

class TableauChaineSimple
{
private:
    Noeud* head;

public: 
    TableauChaine() : head(nullptr) {}

    void ajouter(int valeur)
    {
        Noeud* newNoeud = new Noeud(valeur);
        if(head == nullptr)
        {
            head = newNoeud;
        } 
        else
        {
            Noeud* dernier = head;
            while(dernier->suivant != nullptr)
            {
                dernier = dernier->suivant;
            } 
            dernier->suivant = newNoeud;
        }
    } 

    void affichage()
    {
        Noeud *courant = head;
        while(courant != nullptr)
        {
            cout << courant->data << "  ";
            courant = courant->suivant;
        }
        cout << endl;
    }

    void deleteAll()
    {
        Noeud* courant = head;
        while(courant != nullptr)
        {
            Noeud* suivant = courant->suivant;
            delete courant;
            courant = suivant; 
        }
        head = nullptr;
    }
};

int main()
{
    TableauChaineSimple liste;

    liste.ajouter(10);
    liste.ajouter(20);
    liste.ajouter(30);

    liste.affichage();

    liste.deleteAll();

    return 0;
}