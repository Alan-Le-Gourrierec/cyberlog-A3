#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<vector<int>> M = {{1, 2}, {3, 4}, {5, 6}};
    vector<vector<int>> N = {{1, 2, 3}, {4, 5, 6}};
    vector<vector<int>> Solve(3, vector<int>(3, 0));

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 2; k++) {
                Solve[i][j] += M[i][k] * N[k][j];
            }
        }
    }

    cout << "Matrice résultante :\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << Solve[i][j] << "  ";
        }
        cout << endl;
    }

    return 0;
}