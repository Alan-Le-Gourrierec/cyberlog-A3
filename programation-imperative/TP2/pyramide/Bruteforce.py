import time
PATH = 'programation-imperative/TP2/pyramide/Dictionaire.txt'
f = open(PATH, 'r')
dico = f.read().split("\n")
f.close


def Brutforce(mot, dico): 
    i,t=0,time.time() 
    try:
        while (mot != dico[i]):
            i+=1
    except:
        return "le mot n'existe pas"
    return i, time.time()-t

print(Brutforce("zythums",dico))
