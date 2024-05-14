import random 

def Ocurance(T):
    nbr=0
    for i in range(1,len(T)):
        if(T[i]==T[0]):
            nbr+=1
    return nbr
    
def Moyenne(T):
    sum =0
    for i in range(len(T)):
        sum = sum + T[i]
    return (sum/len(T))

def NewListe():
    T=[]
    for i in range(int(random.uniform(0,10000))):
        T.append(int(random.uniform(0,1000)))
        if(i == 0):
            min,max = T[i],T[i]
        if(T[i]>max):
            max = T[i]
        if(T[i]<min):
            min = T[i]
    T.append(-1)
    return T,min,max

def Monotonie(T):
    for i in range(len(T)-1):
        if T[i+1]>T[i]:
            nbr+=1
    return nbr
    
print("a. afficher la moyenne\nb. afficher le minimum\nc. afficher le maximum\nd. afficher le nombre d'occurences du 1er entier\ne. afficher le nombre de monotonies\nl. affichier la liste et la longuere\nn. Nouvelle liste\nq. quitter (defaut)  \n")
Table,mini,maxi = NewListe()
while True :
    menu = input("entrer l'option que vous souhaité\n")
    match menu:
        case "a":
            print(Moyenne(Table))
        case "b":
            print(mini)
        case "c":
            print(maxi)
        case "d":
            print(Ocurance(Table))
        case "e":
            print(Monotonie(Table))
            print("tkt mon reuf c'est en dev")
        case "l":
            print(len(Table))
        case "n":
            Table,mini,maxi = NewListe()
        case _:
            break     