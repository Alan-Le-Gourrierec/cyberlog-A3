from math import floor, sqrt

def divider(a):
    T = []
    for d in range(1,floor(sqrt(a))):
        if a%d == 0 :
            T.append(d)
    for i in range (len(T)-1,-1,-1):
        T.append(floor(a//T[i]))
    return T
            
print(divider(72047539))