import time
import matplotlib.pyplot as plt

# Alan Le Gourrierec; TP : programation impérative; 13 septembre 2023
temps = time.time()
def Power(a,n):
    t = time.time()
    pwr,i = a,1
    if type(n)==float or n < 0:
        return "ERROR, entier naturels uniquement"   
    for i in range(1,n):            
        pwr = pwr * a
    return time.time()-t

max = 500
a = 500

#### 
labels = [x for x in range(max)]
values = [Power(a,x) for x in range(max)]
plt.plot(labels, values)
plt.show()
plt.xlabel("nombre d'itérations")
plt.ylabel = "time"
####

print(time.time()-temps)