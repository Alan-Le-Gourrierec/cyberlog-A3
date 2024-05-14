#include <iostream>
#include <climits>
#include <typeinfo>

using namespace std;

int main (){
    auto var=0;
    cout<<"entré une valeur pour var"<<endl;
    cin>>var;
    cout<<"notre variable est de type "<<typeid(var).name()<<" => "<<sizeof(var)*CHAR_BIT<<" bytes"<<endl;
    return 0;
}