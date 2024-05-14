#include <iostream>

using namespace std;

int main()
{
    int a = 20;
    int b = 10;

    int* a_ptr = &a;
    cout<<"*a_ptr : " << *a_ptr << ",a : " << a <<endl;
    
    a_ptr = &b;
    cout<<"*a_ptr : " << *a_ptr << ",a : " << a <<endl;
    
    *a_ptr = 30;
    cout<<"*a_ptr : " << *a_ptr << ",b : " << b <<endl;
    return 0;
}