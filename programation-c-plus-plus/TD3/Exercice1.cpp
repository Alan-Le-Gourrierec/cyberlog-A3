#include <iostream> 

using namespace std;

class Node 
{
private:
    string identifiant;
    int x;
    int y;

public:
    TypeNode(string mot, int x, int y){
        this->identifiant = mot;
        this->x = x;
        this->y = y;
    }

    string getMot() const{return mot;}
    int getX() const {return x;}
    int getY() const {return y;}

    void affichage()
    {
        cout<<"identifiant : "<<this->mot<<" | x="<<this->x<<",y="<<this->y<<endl;
    }
};

