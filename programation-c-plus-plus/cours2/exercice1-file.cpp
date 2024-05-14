#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
    ifstream in_file;
    int i = 0;
    string PATH = "/home/alan/Documents/ENSIBS/cyberlog-A3/programation-c-plus-plus/cours2/test.txt";
    test:
    in_file.open(PATH);

    if(in_file.is_open())
    {
        while(!in_file.eof())
        {
            string ligne;
            getline(in_file, ligne);
            cout<<ligne<<endl;
        }
    }
    else
    {
        (i<3) ? (goto test):(cout<<"erreur dans le programme :sob:");
    }
    return 0;
}