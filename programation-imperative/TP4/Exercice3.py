#Le gourrierec Alan - cyberlog26 - 6/11/2023
import random as rd
import time
import matplotlib.pyplot as plt

"""Pour faciliter la comprehension et avoir des exemples comcrèts et plus parlant
que de simple chaîne de caracthère, j'ai décider d'encoder les mots (choisie au
hasard dans le dictionaire) et de les hasher afin que ceci nous renvoie un autre 
dans le quelle il est hasher.
Les tests sont faits avec des valeurs aléatoires"""

# PATH À MODIFIER !!!!

PATH = 'programation-imperative/TP2/pyramide/Dictionaire.txt'
f = open(PATH, 'r')
dico = f.read().split("\n")
f.close

#len dico = 323580 | place ecureuil = 113602

#################################################################################

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

def IWantSquirrel(values,N,dico=dico): #fonction pour trouver la clé d'un mot
    for i in dico:
        if dico[H2(i,N)] == values : return i
    return None

def FoundEmptyTable(Hash):
    for place in range(len(Hash)):
        if Hash[place]==[] : return place
    return rd.randint(0,len(Hash)-1) #choix aléatoire de la table à écraser    

################################################################################

size = 323580 #nombre totale de mot dans le dictionaire 

def Creation(definition):
    return [[] for i in range(definition)]

HashTable = Creation(10)# déclration de notre table de hash   
  
def Ajout(T, key, valeur):
    for i in range(len(T)): #recherche si existant 
        a,b = T[i] 
        if a == key or b == valeur : #si l'instance existe déjà, alors nous ne l'ajoutons pas
            return T 
    T.append((key, valeur))
    return T 

def AutoRemplisage(T, dimention, taile=size,dico=dico):
    for i in range(dimention):
        mot = dico[rd.randrange(0,taile)] #génération du mot de manière aléatoire
        T.append((mot,dico[H2(mot,taile)])) #génération de la valeur et ajout dans le tuple  
    return T

def Recherche(T,key):
    for i in range(len(T)):
        a,b = T[i]
        if a == key:
            return T[i],i
    return None

def Rehash(T,N,dico=dico,HashTable=HashTable):
    print("la clé est : ",N)
    Solve = HashTable[FoundEmptyTable(HashTable)]
    if Solve != []:
        Solve = []
    for i in range(len(T)):
        a,b = T[i]
        Solve.append((a,dico[H2(a,N)]))
    return Solve
        
#################################################################################

print(HashTable[0])
HashTable[0] = AutoRemplisage(HashTable[0],10)
print(HashTable[0])

HashTable[0] = Ajout(HashTable[0], 'test', 'ecureuil')
HashTable[0] = Ajout(HashTable[0], 'test', 'ecureuil') 

print(HashTable[0],"\n")
print(Recherche(HashTable[0],'test'),"\n") #ecureuil n'aparaitras q'une unique fois 

print(Rehash(HashTable[0],rd.randint(0,size)),"\n")
print(HashTable)

print(IWantSquirrel("ecureuil",size))