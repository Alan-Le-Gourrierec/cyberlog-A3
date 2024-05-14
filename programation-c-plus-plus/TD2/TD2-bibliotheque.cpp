#include <iostream>
#include <string>
#include <regex>
#include <fstream>
#include <vector>
#include <map>
#include <utility>
#include <filesystem>

using namespace std;

/*
Le Gourrierec Alan, 11/01/2024

Le code ci-dessous à pour but de répondre au questions des parties 1 et 2 du 
second TP de projet dévelopement C++. Si vous souhaitez l'utiliser, il vous 
faudras modifier les PATH ligne 119 et 120 (représentant respectivement: un
fichier .csv pour le fichier d'entré qui nous à été fournis et le second PATH
représente l'emplacementdu fichier de sorti res.txt).

Pour résoudre ce TD, j'ai en grande majorité utilisé les regex et créer une class
pour potentielment réutiliser certaines données plus tard.
*/

//création d'une classe utilisé pour la question 1.2 afin de potentielement
//pouvoir réutiliser les résultats (l'utilisation de pointeur peu aussi fonctionner)


class TypeNode 
{
private:
    string mot;
    int x;
    int y;

public:
    TypeNode(string mot, int x, int y){
        this->mot = mot;
        this->x = x;
        this->y = y;
    }

    string getMot() const{return mot;}
    int getX() const {return x;}
    int getY() const {return y;}
};

int getCode(string str) 
{
    regex type1("\"Node\",,");
    regex type2("\"Node\\d+\",\\d+,\\d+");
    regex type3("\"traffic\",,");
    //regex type4("(\"Node\\d+\",)*\"Node\\d+\"");
    regex type4("\"Node\\d+\",\"Node\\d+\"");
    regex type5("\"connection\",,");

    int code = 0;
    if (regex_match(str, type1)) {
        return 1;
    } else if (regex_match(str, type2)) {
        return  2;
    } else if (regex_match(str, type3)) {
        return 3;
    } else if (regex_match(str, type4)) {
        return 4;
    } else if (regex_match(str, type5)) {
        return 5;
    }
    return 6;
}

TypeNode Extract(string str)
{

    //le but est d'extraire d'un type 2 (cf sujet), le nom du noeud et ses coordonnées

    regex pattern("\"(Node\\d+)\",(\\d+),(\\d+)");
    smatch matches;
    TypeNode solve("", 0, 0);

    if (regex_match(str, matches, pattern)) 
    {
        solve = TypeNode(matches[1], stoi(matches[2]), stoi(matches[3]));
    }
    return solve;
}

vector<string> ExtractType4(string str) 
{

    //le but est d'extraire d'un type 4, le nom de chaques noeuds en relation

    regex pattern("\"(Node\\d+)\"");
    smatch matches;
    vector<string> solve;

    while (regex_search(str, matches, pattern)) 
    {
        solve.push_back(matches[1]);  
        str = matches.suffix().str();
    }

    return solve;
}

map<string, pair<int, int>> Plot(const string& PATH, ifstream& in_file) {

    /*
    Dans cette fonction, notre objectif est de récupérer les coordonnées de 
    tous les node présent. Pour se faire, nous allons utiliser un dictionnaire
    avec comme paramètre d'entré un string et en sortie, une paire de int
    (coordonnée x et y).

    Pour se faire, nous allons lire le fichier afin de trouver tout les points 
    de type 2 (ou de la forme NodeX Y,Z)
    */

    map<string, pair<int, int>> dictionnaire;
    in_file.open(PATH);

    if (not(in_file.is_open())) 
    {
        cerr << "ERREUR, le fichier n'existe pas." << endl;
        return dictionnaire;
    }

    string ligne;
    while (!in_file.eof()) 
    {
        string ligne;
        getline(in_file,ligne);

        int type = getCode(ligne);
        if (type == 2) 
        {
            TypeNode Node = Extract(ligne);
            dictionnaire[Node.getMot()] = make_pair(Node.getX(), Node.getY());
        }
    }
    in_file.close();
    return dictionnaire;
}

void OutToGNUPlot(map<string, pair<int,int>> dictionnaire,string PATH, ifstream &in_file, string out_PATH, ofstream &out_file)
{
    /*
    Ceci est la fonction permetant de ressortir le fichier en .dat.
    */
    in_file.open(PATH);
    out_file.open(out_PATH);
    bool connection = false; //condition pour ne prendre en compte que les connections 

    if(not(in_file.is_open()) || not(out_file.is_open()))
    {
        cerr<< "ERROR, le path du fichier est mauvais"<< endl;
        return;
    }
    while(!in_file.eof())
    {
        string ligne;
        
        getline (in_file, ligne);
        int type = getCode(ligne);

        if(type == 5)
        {
            connection = true;
        }
        if (type == 4 and connection == true)
        {
            vector<string> result = ExtractType4(ligne);
            int size = result.size();

            for(int i =0; i<size; i++)
            {
                int value1 = dictionnaire[result[i]].first;
                int value2 = dictionnaire[result[i]].second;
                out_file<<value1<<"  "<<value2<<endl;
            }
            out_file<<endl;
        }
    }
    
    out_file.close();
    in_file.close();
}

/*
Cette partie est dédié au fonctions utilisé pour la signature des fichiers.
Nous y retrouverons les diverses fonctions utilisé pour réaliser les algorithmes 
relevant de la signature de fichier.
*/