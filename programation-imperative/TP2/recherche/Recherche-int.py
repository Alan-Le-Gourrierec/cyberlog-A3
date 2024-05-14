import random

def RandList():
    A = []
    for i in range(int(random.uniform(0,20))):
        A.append(int(random.uniform(0,20)))
    return A

def Recherche(n,A):
    print(A)
    tmp,i = None,0
    try:
        while n != tmp:
            tmp = A[i]
            i+=1
    except:
        return "la valeur que vous demandé n'existe pas"
    return i

A= RandList()
print(A)
n = int(input("quelle valeurs souhaitez vous ?\n"))
print(Recherche(n,A))