#include <string>
#include <iostream>
#include <vector>
#include <regex>

using namespace std;

int main() {
    string mot = "\'Node8',\'Node1',\'Node3',\'Node7',\'Node7',\'Node6'";
    regex pattern("\\\\'([^']+)'");
    vector<string> nodes;

    sregex_iterator iter(mot.begin(), mot.end(), pattern);
    sregex_iterator end;

    while (iter != end) {
        nodes.push_back((*iter)[1].str());
        ++iter;
    }

    if (nodes.size() > 1) {
        cout << "Node at index 1: " << nodes[1] << endl;
    } else {
        cout << "Not enough nodes found." << endl;
    }
    return 0;
}
