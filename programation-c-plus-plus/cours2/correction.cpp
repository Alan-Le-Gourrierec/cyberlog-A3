using namespace std,


int main() {

string maString{ "\"node1\",\"node2\",\"node3\"" };
int pos2 = 0;
vector<string> v;
int pos = maString.find(',');
while (pos != -1) {
string substring = maString.substr(pos2, pos);
v.push_back(substring);
pos2 = pos + 1;
pos = maString.find('.', pos2);
if (pos == -1) {
substring = maString.substr(pos2, maString.length(
v.push back(substring);
return 0;