#include <iostream>

#include "TD2-bibliotheque.cpp"

using namespace std;
namespace fs = filesystem;

string outNameFile(string name)
{
    smatch matches;
    regex pattern(R"(([\w.]+)\.([\w./]+))");

    if(regex_search(name, matches, pattern))
    {
        return matches[1]; 
    }
}

void gnuExportDirectory(const string& directory)
{
    for(const auto& entry : fs::directory_iterator(directory))
    {
        ifstream in_file;
        ofstream out_file;
        string out_PATH = "resultat/" + outNameFile(entry.path()) + ".dat";

        map<string, pair<int,int>> dictionnaire = Plot(entry.path(), in_file);

        OutToGNUPlot(dictionnaire, entry.path(), in_file, out_PATH, out_file);
    }
}

int main()
{
    string in_PATH = "Examples";
    gnuExportDirectory(in_PATH);

    return 0;
}