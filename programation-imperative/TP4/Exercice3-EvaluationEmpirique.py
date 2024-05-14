import random as rd
import time
import matplotlib.pyplot as plt
import math

PATH = 'programation-imperative/TP2/pyramide/Dictionaire.txt'
f = open(PATH, 'r')
dico = f.read().split("\n")
f.close

size = len(dico)
def H2(key, N):
    # precondition: key is an alphanumeric string
    # N is the size of the hashtable
    hashsum = 0
    l = len(key)
    # For each character in the key
    for idx in range(l):
        # Add (index + length of key) ^ (current char ascii code)
        hashsum += (idx + len(key)) ** ord(key[idx])
        # Perform modulus to keep hashsum in range [0, N - 1]
    hashsum = hashsum % N
    return hashsum

def Creation(dimention):
    HashTable = []
    for i in range(dimention): 
        HashTable.append([])
    return HashTable #juste un tableau de tableau vide 

def AutoRemplisage(T, dimention,number , taile=size,dico=dico):    
    t= time.time()
    for i in range(dimention):
        mot = dico[rd.randrange(0,taile)] #génération du mot de manière aléatoire
        T.append(H2(mot,number)) #génération de la valeur et ajout dans le tuple  
    return time.time() -t

#evaluation empirique pour N = const
HashTable=Creation(10)
iteration,moy,N = 1000,100,1000
quantite=10 #permetras d'obtenir une moyenne afin d'améliorer le graph finale
values = []

labels = [x for x in range(iteration)]
for i in range(iteration):
    tmp = [AutoRemplisage(HashTable[0],quantite,N) for x in range(moy)]
    values.append(sum(tmp)/moy)

plt.plot(labels, values)
plt.xlabel = "nombre d'itérations"
plt.ylabel = "time"
plt.show()

print("le temps moyen est de : ",sum(values)/iteration)

#evaluation empirique pour N entre 10² et 10⁵
HashTable=Creation(10)
iteration,moy,N = 1000,100,100
quantite=10 #permetras d'obtenir une moyenne afin d'améliorer le graph finale
values,tmp = [],[]

labels = [x for x in range(iteration)]
for i in range(iteration):
    for j in range(moy):
        tmp.append
    N += 10
    values.append(sum(tmp)/moy)
    print(values)

plt.plot(labels, values)
plt.xlabel = "nombre d'itérations"
plt.ylabel = "time"
plt.show()

print("le temps moyen est de : ",sum(values)/iteration)
