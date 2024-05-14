from math import floor
import time
# Alan Le Gourrierec; TP : programation impérative; 13 septembre 2023

def Multiplication(a,b):
    prod,t = 0,time.time()
    while b > 0 :
        prod = prod + a
        b = b//2
        a = a+a
    return time.time()-t

print(Multiplication(19,23)) 