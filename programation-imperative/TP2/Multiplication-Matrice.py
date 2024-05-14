import numpy as np
A=np.array([[5,1],[2,3],[3,4]])
B=np.array([[1,2,0],[4,3,-1]])

def Multiplication(A,B):
    n1,m = np.shape(A)
    p,n2 = np.shape(B)
    C = []
    
    if n1!=n2:
        return "ERREUR : les dimentions des listes A et B ne sont pas valides"
    
    else:
        for i in range(n1):
            Liste = []
            
            for j in range(n1):
                sum = 0
                
                for k in range(p):
                    sum = sum + A[j,k]*B[k,i]
                    
                Liste.append(sum)
            C.append(Liste)
        return C
       
print(Multiplication(A,B))
                
            