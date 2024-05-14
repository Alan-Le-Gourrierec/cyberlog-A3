PATH = 'programation-imperative/TP2/pyramide/Dictionaire.txt'
f = open(PATH, 'r')
dico = f.read().split("\n")
f.close


'''Cette algorithme de Dicotomie permet de résondre une recherche dans un dictionaire en 
environ ~1.35.10**-5s'''
def Dicothomie(mot,dico):
    placem,placeM = 0,len(dico) #initialisation de l'encadrement de la liste
    place = (placem+placeM)//2 #définition de place qui désigne la position que la liste va pointé
    s,splus1 = None,dico[place] #définition de deux string qui permetrons de savoir si un mot exite ou non
    
    while(mot != dico[place]): 
        if(mot>dico[place]):
            placem = place 
            
        elif(mot<dico[place]):
            placeM = place
            
        if(s == splus1):
            return 0
        
        place=(placem + placeM)//2 
        s = splus1 
        splus1 = dico[place] 
          
    return 1           
        
'''recherche dans tout le dictionnaire si un mot existe, prends pour le pire des cas ~1.04.10**-2s '''
def Brutforce(mot, dico): 
    i,t=0 
    try:
        while (mot != dico[i]):
            i+=1
    except:
        return 1
    return 0

def Jeu(dico):
    motmoins1 = []
    
    while True:
        mot = input("entrer le mot :\n")
        tmp = 1
        Table_mot = list(mot)
        
        if len(mot) != len(motmoins1)+1:
            return "Dommage, la longueure du mot ne conviens pas"
        #Dicothomie est plus rapide en générale pour parcourir le dictionaire
        elif Dicothomie(mot, dico) == 0: 
            return "Dommage, ce mot n'existe pas"
        #les mots seront courts donc l'algorithme Brutforce seras plus rapide
        for i in range(len(mot)):
            tmp+=Brutforce(Table_mot[i],motmoins1)
            if tmp == -1:
                return "Dommage, les lettres du mot ne conviennent pas"
        
        motmoins1 = Table_mot

Jeu(dico)