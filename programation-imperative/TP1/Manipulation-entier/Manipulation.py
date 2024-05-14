from math import sqrt,floor

def Permute (T):
    Table = []
    for i in range(len(T),0,-1):
        Table.append(T[i-1])
        a = "".join(Table)
    return int(a)

def Decomposition(nombre):
    #retourne la division en facteurs premiers de l'entier
    facteurs = []
    diviseur = 2
    while diviseur * diviseur <= nombre:
        if nombre % diviseur == 0:
            facteurs.append(diviseur)
            nombre = nombre // diviseur
        else:
            diviseur += 1
    if nombre > 1:
        facteurs.append(nombre)
    return facteurs

def Euclide(n1,n2):
    a = max(n1,n2)
    b = min(n1,n2)
    while b!=0:
        a, b = b, a%b
    if b == 1:return 1
    else : return a

def LongEuclide(n1,n2):
    u0=1;u1=0
    v0=0;v1=1
    a = max(n1,n2)
    b = min(n1,n2)
    while b!=0:
        q = a // b
        a ,b = b, a%b
        u0 , u1 = u1, u0-q*u1
        v0 , v1 = v1, v0-q*v1
    return u0,v0

a = int(input("entrer la valeur a :\n"))
b = int(input("entrer la valeur b :\n"))
print(Euclide(a,b))
print(LongEuclide(a,b))