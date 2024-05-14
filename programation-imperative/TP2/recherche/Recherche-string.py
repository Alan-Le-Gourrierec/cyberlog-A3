def Recherche(mot,liste):
    i=0
    try:
        while mot != liste[i]:
            i+=1
        return i+1
    except:
        return "Desole, vôtre mot n'existe pas dans la liste"

mot = "les points virgules me manque "
T=["test","baltimore","camion","oud-point","abri-bus","cailloux"]
print(Recherche(mot,T))
test = "Aufmerksamkeit !! die heilige Betonplatte kommt!!"

def RechercheChaine(mot,liste,start):
    T,L=[],[]
    T=list(mot)
    L=list(liste)
    if len(T) == 0 or len(L) == 0:
        return "longueure des arguments insufisants"
    for i in range(start,len(L)):
        a = 0
        
        while T[a] == L[i+a]:
            if T[a] == L[i+a] and a == len(T)-1:
                return i
            a+=1
    return None
    
def Remplacement(mot,phrase,remplacer):
    i = 0
    if len(mot) ==0 or len(phrase)==0 :
        return "longueure des arguments insufisante"
    
    while i != None:
        gauche,droite = [],[]
        
        i = RechercheChaine(mot,phrase,i)
        if i == None:
            return phrase
        #découpage du string en deux chaine de caracthères (gauche et droite en suprimant le "mot" au centre) 
        else :
            for j in range(i):
                gauche.append(phrase[j])
                
            for j in range(i+len(mot),len(phrase)):
                droite.append(phrase[j])
                
        phrase = "".join(gauche)+remplacer+"".join(droite)
             
mot = "les points virgules me manque "
T=["test","baltimore","camion","oud-point","abri-bus","cailloux"]
test = "Aufmerksamkeit !! die heilige Betonplatte kommt!!"

print(Recherche(mot,T))
 
print(RechercheChaine("",test,0))

print(Remplacement("d",test,"e"))
    

        
    