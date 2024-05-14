
<b><u>exercice 2-1 </b></u> 

```cpp
#include <iostream>

using namespace std;

int main(){
    int a;
    double b;
    char c[20];
    cin>>a>>b>>c;
    cout<<"int "<<a<<" double "<<b<<" table char "<<c<<endl;
    return 0;
}
```


<b><u>exercice 2-2 </b></u> 
execution du programme avec 1 | 2.5 | ensibs
![[Pasted image 20240110155752.png]]

execution du programme avec 2.5 | 1 | ensibs
![[Pasted image 20240110155932.png]]

Nous remarquons que le programme modifie les divers valeurs, 2.5 est transformé en sa valeur entière 2, et 1 est transformé en 0.5.
<u><b>exercice 3-1</b></u>

```cpp
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
```

<u><b> exercice 3-2 </u></b>

```cpp
#include <iostream>
#include <iomanip>
#include <limits>
#include <cmath>

int main() {

long double pi = 3.14159265358979323846264338327950288419716939937510582L;

// Obtenir la précision maximale pour le type long double
int max_precision = std::numeric_limits<long double>::digits10;

// Affichage avec la précision maximale
std::cout << "valeur aproximative de pi : " << std::setprecision(max_precision) << pi << std::endl;
return 0;

}
```

<u><b> exercice 3-3 </u></b>
```cpp
#include <iostream>
#include <climits>

using namespace std;

int main() {
    cout<< " int min" << INT_MIN << " int max" << INT_MAX <<endl;
    cout<< " int min" << INT_MIN-1 << " int max" << INT_MAX+1 <<endl;

    cout<< " long long min " << LLONG_MIN << " long long max " << LLONG_MAX<<endl; 
    cout<< " long long min " << LLONG_MIN-1 << " long long max " << LLONG_MAX+1 <<endl;
}
<u><b> exercice 4-1 </u></b>
```

La augment simplement il réussi donc à comprendre la valeur de chacun 
*![[Pasted image 20240110173940.png]]

<u><b> exercice 4-1 </u></b>

```cpp
#include <iostream>
#include <map>
#include <string>
  
using namespace std;
  
int main() {
map<string,string> semainier;
semainier["Lundi"] = "papaye";
semainier["Mardi"] = "orange";
semainier["Mercredi"] = "pêche";
semainier["Jeudi"] = "banane";
semainier["Vendredi"] = "pomme";
semainier["Samdi"] = "clémentine";
semainier["Dimanche"] = "poire";
  
string array[7]= {"Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samdi","Dimanche"};
int var;
cin >> var;
cout << semainier[array[var-1]] << endl;
return 0;
}
```

<u><b> exercice 5-1 </u></b>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<double> Table;
    cout << "Entrez des valeurs, et lorsque vous souhaitez arrêter, entrez 0 :" << endl;
    double var = 1;
    double sum = 0;

    while (var != 0) {
        cin >> var;
        sum += var;
        Table.push_back(var);
    }

    // Affichage de la somme
    cout << "La somme de tous les nombres est : " << sum << endl;

    // Affichage des valeurs dans l'ordre d'entrée
    cout << "Les valeurs entrées dans l'ordre sont : ";
    for (int i = 0; i < Table.size(); ++i) {
        cout << Table[i] << "  ";
    }

    // Tri du vecteur
    sort(Table.begin(), Table.end());

    // Affichage des valeurs triées
    cout << "\nLes valeurs triées sont : ";
    for (int i = 0; i < Table.size(); ++i) {
        cout << Table[i] << "  ";
    }

    return 0;
}
```

<u><b> exercice 5-2 </b></u>

```cpp
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
```

![[Pasted image 20240110172636.png]]
