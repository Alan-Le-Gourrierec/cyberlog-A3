import time
PATH = 'programation-imperative/TP2/pyramide/Dictionaire.txt'
f = open(PATH, 'r')
d = f.read().split("\n")

def searchDicoRecursive(word, l=d):
    t = time.time()
    if word==l[len(l)//2] :
        return "found", time.time() -t
    elif (len(l)==1) and (word!=l[0]) :
        return "not found", time.time()-t
    if word<l[len(l)//2] :
        return searchDicoRecursive(word,l[:len(l)//2])
    else :
        return searchDicoRecursive(word,l[len(l)//2:])

print(searchDicoRecursive("geahdkchbezvha"))