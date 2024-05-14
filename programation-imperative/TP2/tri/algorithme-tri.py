import random,time

def Liste():
    L=[]
    for i in range(26):L.append(chr(97+i))
    random.shuffle(L)
    return L

def Selection(jeu):
    t=time.time()
    for i in range(len(jeu)):
        mini = i
        for j in range(i,len(jeu)):
            if jeu[mini] > jeu[j]:
                mini = j
        jeu[i],jeu[mini]=jeu[mini],jeu[i]
    return jeu, time.time()-t

def Insertion(jeu):
    t = time.time()
    Liste=[None]*len(jeu)
    for i in range(len(jeu)):
        tmp = ord(jeu[i])-97
        Liste[tmp] = jeu[i]
    return Liste, time.time()-t

def Fusion(jeu):
    return "tkt mon reuf c'est en dev"

print(Selection(Liste()))
print(Insertion(Liste()))
print(Fusion(Liste()))