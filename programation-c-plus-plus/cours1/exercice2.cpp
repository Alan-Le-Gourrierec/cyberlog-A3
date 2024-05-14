#include <iostream>

using namespace std;

int main() {
    int Table[2][2] = {{0, 1}, {2, 3}};
    int i = 0;
    loop:
        cout << &Table[i][0] << "  " << &Table[i][1] << "\n";
        if (i == 0) {
            i++;
            goto loop;
        }
    return 0;
}