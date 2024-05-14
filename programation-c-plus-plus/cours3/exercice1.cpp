#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void printFile(string PATH, ifstream &in_file)
{
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
}

int main()
{   
    ifstream in_file;
    string PATH = "/home/alan/Documents/ENSIBS/cyberlog-A3/programation-c-plus-plus/cours2/test1.txt";
    
    printFile(PATH, in_file);    
    return 0;
}