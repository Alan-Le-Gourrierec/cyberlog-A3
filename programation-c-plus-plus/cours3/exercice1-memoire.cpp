#include <iostream>

using namespace std;

int main()
{
    char s1[15];
    char s2[5];

    cout<<"valeur 1";
    cin.getline(s1,"\n");

    cout<<"valeur 2";
    cin.getline(s2,"\n");

    cout<<"s1="<<s1<<endl;
    cout<<"s2="<<s2<<endl;

    return 0;
}