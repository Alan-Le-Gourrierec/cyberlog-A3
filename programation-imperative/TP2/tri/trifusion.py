import random, time
def Liste():
    L=[]
    for i in range(26):L.append(chr(97+i))
    random.shuffle(L)
    return L

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    
    milieu = len(liste) // 2
    l,r = tri_fusion(liste[:milieu]), tri_fusion[milieu:]
    return fusionner(l, r)

def fusionner(gauche, droite):
    resultat = []
    i = j = 0
    
    while i<len(gauche) and j<len(droite):
        if gauche[i]<droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    
    return resultat

# Exemple d'utilisation :
print(tri_fusion(Liste()))