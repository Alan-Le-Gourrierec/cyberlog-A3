#include <iostream>

#include "TD2-bibliotheque.cpp"

int main()
{
    string PATH = 
    ofstream out_filedat;
    string out_PATHdat="resultat/datafile_gnu.dat";

    map<string , pair<int,int>> dictionnaire = Plot(PATH, in_file);

    OutToGNUPlot(dictionnaire,PATH,in_file,out_PATHdat,out_filedat);

    return 0;
}