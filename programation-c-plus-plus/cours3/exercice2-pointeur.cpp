#include <iostream>

using namespace std;

void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

int main()
{
    int x = 10;
    int y = 20;
    
    cout<<"x : "<<x<<"\ny : "<<y<<endl;
    
    swap(x,y);
    cout<<"x : "<<x<<"\ny : "<<y<<endl;

    return 0;
}