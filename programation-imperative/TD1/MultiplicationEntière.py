# Alan Le Gourrierec; TP : programation impérative; 13 septembre 2023
import time
import matplotlib.pyplot as plt

def Multiplication (a,b):
    tmp,t = 0,time.time()
    if type(a)=="int" or a < 0 or type(b)=="int" or b < 0:
        return "ERROR, values of a or b are not avalaible"
    for i in range(b):
        tmp = tmp + a 
    return time.time()-t

iterations_amont = 789
b = 654
labels = [x for x in range(iterations_amont)]
values = [Multiplication(iterations_amont,b) for x in range(iterations_amont)]
plt.plot(labels, values)
plt.xlabel = "nombre d'itérations"
plt.ylabel = "time"
plt.show()