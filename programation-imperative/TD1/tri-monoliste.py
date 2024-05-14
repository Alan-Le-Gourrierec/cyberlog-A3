import time
import random 
import matplotlib.pyplot as plt

def generation(amount): 
    A =[]
    for i in range(amount):
        A.append(int(random.uniform(0,100)))
    return A

def Ordre(A):
    t=time.time()
    for i in range(len(A)):
        for j in range (i,len(A)):
            if j == i :
                x = A[j]
            elif x > A[j]:
                temp=A[i]
                A[i]=A[j]
                A[j]=temp
                x=A[i]
                x=A[i]
    return time.time()-t

size_A,iteration =100,100
liste_A = generation(size_A)
print(liste_A)

labels = [x for x in range(iteration)]
values = [Ordre(liste_A) for x in range(iteration)]
plt.plot(labels, values)
plt.xlabel = "nombre d'itérations"
plt.ylabel = "time"
plt.show()
