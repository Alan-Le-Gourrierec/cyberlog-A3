dictionaire = {"saucisse" : "saussage", "test" : "test", "camion" : "trunk", "Cascadie" : "Cascadia",
               "soleil": "sun", "ecureuil" : "squirrel"}

def AjoutMot (word,trad, dico=dictionaire): 
    tmp = word in dico.keys() # je voulais l'utilisé directement en condition mais ca ne marchais pas
    if tmp == False :
        dico[word] = trad
    return dico

def AffichageCle(dico=dictionaire):
    for i in dico.keys():
        print(dico[i])

def SuppOccurances(char, dico=dictionaire):
    List = []
    for i in dico.keys():
        Tmp = list(i)
        if Tmp[0] == char:
            List.append(i)
    for i in range(len(List)):
        del(dico[List[i]])
    return dico
    
######## test #########
print(dictionaire,'\n')
AjoutMot("faim","hungry")
print(dictionaire,"\n")
print(SuppOccurances("s"))