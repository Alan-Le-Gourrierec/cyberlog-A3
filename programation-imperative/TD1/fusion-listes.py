import time
import random 
import matplotlib.pyplot as plt

def Fusion(A,B):
    C = []
    C.extend(A + B)
    return C

def generation(amount): 
    A =[]
    for i in range(amount):
        A.append(int(random.uniform(0,100)))
    return A

def Ordre(A,B):
    t=time.time()
    C = Fusion(A,B)
    for i in range(len(C)):
        for j in range (i,len(C)):
            if j == i :
                x = C[j]
            elif x > C[j]:
                temp=C[i]
                C[i]=C[j]
                C[j]=temp
                x=C[i]
    return time.time()-t

size_A,size_B,iteration = 200,200,1000
liste_A,liste_B =generation(size_A),generation(size_B)
print(liste_A,liste_B)

labels = [x for x in range(iteration)]
values = [Ordre(liste_A,liste_B) for x in range(iteration)]
plt.plot(labels, values)
plt.xlabel = "nombre d'itérations"
plt.ylabel = "time"
plt.show()