#include <iostream>
#include <string>
#include <regex>
#include <fstream>
#include <vector>
#include <map>
#include <utility>

#include "TD2-bibliotheque.cpp"

using namespace std;

/*
Le Gourrierec Alan, 11/01/2024

Le  code ci-dessous est le main de mon programme utilisé pour les divers test unitaires.
Il y à donc dans un premier temps, un test pour la pertie 1 et 2. Il y a aussi un autre fichier
nommé dijkstra.cpp pour réssoudre le problème du chemin le plus court. 
*/

int main() 
{
    /*dans un premier temps, nous allons principalement utiliser les regex
    dans le but de résoudre les divers problèmes (cf TD2).
    - la question une aura pour but de revoyer un entier */
    //question 1.1 test

    cout << getCode("\"Node\",,") << endl;
    cout << getCode("\"Node1\",38,34") << endl;
    cout << getCode("\"traffic\",,") << endl;
    cout << getCode("\"Node1\",\"Node2\"") << endl;
    cout << getCode("\"connection\",,") << endl;
    cout << getCode("feur") << endl;
    
    //question 1.2 testtable

    TypeNode Node = Extract("\"Node1\",38,34");

    cout<< Node.getMot() << endl;
    cout<< Node.getX() <<endl;
    cout<< Node.getY() <<endl;

    //question 1.3 test

    vector<string> result = ExtractType4("\"Node1\",\"Node2\",\"Node3\"");

    for (const auto& element : result) 
    {
        cout << element << " ";
    }
    cout << endl;

    /*
    Dans la seconde partie de ce TP, nous allons utilisé ce que nous avons fait lors de
    la première partie dans le but de l'apliquer à un cas pretique. C'est à dire à un fichier
    utilisé par GNU plot.
    */

    //question 2.1 et 2.2. C'est deux questions sont très lié, il est donc logique de le lier.
    //la question 2.3 elle aussi est très proche il suffit d'adapter légèrement le code.

    ifstream in_file;
    ofstream out_file;
    string PATH = "/home/alan/Documents/ENSIBS/cyberlog-A3/programation-c-plus-plus/TD2/Examples/testv44.csv";
    string out_PATH="/home/alan/Documents/ENSIBS/cyberlog-A3/programation-c-plus-plus/TD2/resultat/result.txt";

    int code[6] = {0,0,0,0,0,0};

    in_file.open(PATH);
    out_file.open(out_PATH);

    if (in_file.is_open() && out_file.is_open())
    {
        while(!in_file.eof())
        {
            string ligne;
            getline(in_file,ligne);
            switch (getCode(ligne)) //switch case pour obtenir le nombre d'itération de chaque type
            {
                case 1: code[0]+=1; break;
                case 2: code[1]+=1; break;
                case 3: code[2]+=1; break;
                case 4: code[3]+=1; break;
                case 5: code[4]+=1; break;
                default:code[5]+=1; break;
            }
        }
    }
    else
    {
        cout<<"ERREUR, le(s) fichier(s) n'existe pas."<<endl;
    }
    
    for(int i = 0; i<6; ++i)
    {
        cout<<"type "<<i+1<<" : "<<code[i]<<endl;
        out_file<<"type "<<i+1<<" : "<<code[i]<<endl;
    }

    in_file.close();
    out_file.close();

    /*
    question 2.4 Pour résoudre cette question, je vais utiliser les dictionnaire proposé la 
    bibliothèque map de C++. Elle me premetras d'assossier par exemple Node1 à ses coordonnée

    Ceci utilise principalement 2 fonctions : Plot et OutToGNUPlot
    */
    
    ofstream out_filedat;
    string out_PATHdat="/home/alan/Documents/ENSIBS/cyberlog-A3/programation-c-plus-plus/TD2/resultat/datafile_gnu.dat";

    map<string , pair<int,int>> dictionnaire = Plot(PATH, in_file);

    OutToGNUPlot(dictionnaire,PATH,in_file,out_PATHdat,out_filedat);

    return 0;
}