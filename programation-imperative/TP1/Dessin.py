def Carre(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print("")

def Triangle(n):
    s = 1
    for j in range(n):
        for i in range(s):
            print("* ",end="")
        s+=1
        print("")

def Piramide(n):
    s= 0
    if n%2 == 1: parity = 1
    else: parity = 2
    for i in range(int(n/2)+1):
        
        for j in range(n):
            StarPosition = int(n/2)-s
            amount = parity + 2 * s
            if(j == StarPosition):
                for k in range(amount):
                    print("*", end="")
                    
            else:print(" ",end="")
        s+=1
        print("")
            
def CarreVide (n):
    for i in range(n):
        if(i==0 or i==n-1):
            for j in range(n): print("*",end=" ")  
        else:
            for j in range(n):
                if(j == 0 or j == n-1):print("* ",end="")
                else:print("  ",end="")
        print("")

def Diagonal(n):
    placement = 0
    for i in range(n):
        j=0
        
        while(j<placement):print("  ",end="");j+=1
        print("**")
        placement+=1
        
def Losange(n):
    Piramide(n)
    if(n%2 == 1 ): amount = n-2
    else: amount = n
    for i in range(int(n/2)):
        for j in range(n):
            Startposition = i+1
            k=0
            
            while(j==Startposition and k<amount):
                print("*",end="")
                k+=1
                
            print(" ",end="")
        amount-=2
        print("")