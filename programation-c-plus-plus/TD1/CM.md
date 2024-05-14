en gros, pour appeler les bibliothèque il faut faire : 
```c++
#include <iostream>

int main() {
	//code
	return 0;
}
```

Le print est tjr dégueulasse :
```c++
#include <iostream>

void main(){
	cout<<"hello world"<<"\n";
}
```

L'input :
```c++
#include <iostream>

int main(){
	cin>>data1;
	cout<<data1<<endl;
	return 0;
}
```

on a :
- int 
- char
- string
- bool
- double 
- long int
- long long int
- short int

## Tableau 
Taille fixe ... donc on va faire des pointeurs

## pour les fichiers

```cpp
#include <fstream>

in_file.open(filebame)
```