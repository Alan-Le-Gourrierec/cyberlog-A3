#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector <int> Table = {1,2,3,4};
    cout<<Table.size()<<"\n";
    Table.push_back(5);
    cout<<Table.size()<<"\n";
    return 0;
}