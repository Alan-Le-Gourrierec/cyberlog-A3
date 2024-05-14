import random

def Shuffle(word):
    L=list(word)
    random.shuffle(L)
    return L

def HachageNumber(word): #le mot est convertie automatique  liste dans la partie 2.2 => c'est donc plus rapide de faire comme ceci
    somme = 0 
    for i in range(len(word)):
        somme += ord(word[i])*(256**i)
    return somme%255

def Hachage(word):
    print(word)
    return HachageNumber(word)%255
                 
def BetterHachage(word):
    return sum(map(ord,list(word)))%255

word= "ecureuil"
print(Hachage(word))
print(Hachage("".join(Shuffle(word))))
print(BetterHachage(word))