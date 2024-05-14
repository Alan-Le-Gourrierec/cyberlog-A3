#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main () {
    ifstream in_file;
    ofstream out_file;
    int i = 0;
    string PATH = "/home/alan/Documents/ENSIBS/cyberlog-A3/programation-c-plus-plus/cours2/test.txt";
    string PATH2 = "/home/alan/Documents/ENSIBS/cyberlog-A3/programation-c-plus-plus/cours2/test2.txt";

    test:
    in_file.open(PATH);
    out_file.open(PATH2); 

    if(in_file.is_open() && out_file.is_open())
    {
        while(!in_file.eof())
        {
            string ligne;
            getline(in_file, ligne);
            cout<<ligne<<endl;
            out_file<<ligne<<endl;
        }
    }
    else
    {
        i++;
        bool tmp = (i<3) ? (goto test):(cout<<"erreur dans le programme :zob:");
    }
    in_file.close();
    out_file.close();
    return 0;
}