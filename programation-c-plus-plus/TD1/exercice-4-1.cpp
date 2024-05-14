#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    map<string,string> semainier;
    semainier["Lundi"] = "papaye";
    semainier["Mardi"] = "orange";
    semainier["Mercredi"] = "pêche";
    semainier["Jeudi"] = "banane";
    semainier["Vendredi"] = "pomme";
    semainier["Samdi"] = "clémentine";
    semainier["Dimanche"] = "poire";

    string array[7]= {"Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samdi","Dimanche"};
    int var;
    cin >> var;
    cout << semainier[array[var-1]] << endl;
    return 0;
}