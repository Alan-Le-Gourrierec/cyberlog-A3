#include <iostream>

using namespace std;

int main() {
    int i = 0;
    int a = 1;
    int b = 2;

    test:
        cout << "C'est un banger" << endl;
        goto end;

    retest:
        cout << "Mais je vais me faire tuer" << endl;

    end:
        (i == 0) ? ((a == b) ? (goto test) : (goto retest)) : 0;

    return 0;
}
