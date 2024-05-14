import time

PATH = 'programation-imperative/TP2/pyramide/Dictionaire.txt'
f = open(PATH, 'r')
dico = f.read().split("\n")
f.close

def Dicothomie(mot,dico):
    placem,placeM,t = 0,len(dico),time.time() #initialisation de l'encadrement de la liste
    place = (placem+placeM)//2 #définition de place qui désigne la position que la liste va pointé
    s,splus1 = None,dico[place] #définition de deux string qui permetrons de savoir si un mot exite ou non
    
    while(mot != dico[place]): 
        if(mot>dico[place]):
            placem = place 
            
        elif(mot<dico[place]):
            placeM = place
            
        if(s == splus1):
            return "le mot n'existe pas", time.time()-t
        
        place=(placem + placeM)//2 
        s = splus1 
        splus1 = dico[place]
          
    return place, time.time() -t

print(Dicothomie("zhbavjebvbezb ejb",dico))