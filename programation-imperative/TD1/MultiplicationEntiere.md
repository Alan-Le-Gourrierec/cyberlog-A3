# Multiplication Entière

le but de ce programe est de déterminer si les 2 nombres que nous multiplions sont bien de entiers :
- nous vérifions le type des variables a et b
- (a,b) ∈ N

De plus, nous pouvons, si nous faison une boucle décroissante la fonction s'arreteras dans tout les cas lorsque l'incrémenteur de boule `i` atteindras 0. 

```python
import time
import matplotlib.pyplot as plt

def Multiplication (a,b):
    tmp,t = 0,time.time()
    if type(a)=="int" or a < 0 or type(b)=="int" or b < 0:
        return "ERROR, values of a or b are not avalaible"
    for i in range(b,0,-1):
        tmp = tmp + a 
    return time.time()-t


iterations_amont = 789
valeur = 654


labels = [x for x in range(iterations_amont)]
values = [Multiplication(iterations_amont,valeur) for x in range(iterations_amont)]
plt.plot(labels, values)
plt.show()
plt.xlabel = "nombre d'itérations"
plt.ylabel = "time"
```

Le fonctionement de de ce programme est simple : 
- nous avons deux varaibles : itération_amount qui représente le nombre de fois que nous allons incrémenter notre programme 
- valeur qui est la valeur de base utilisé dans notre programme.

`Ce qui nous intérèsse est le temps d'éxécution du programme d'ou le fait que nous ne retournons que ce dernier.`

il possède une complexité linéaire comme nous pouvons le voir avec le graphique ci-dessou