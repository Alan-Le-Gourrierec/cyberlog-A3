import random 

T,min,max=[],0,0
for i in range(int(random.uniform(0,100000))):
    T.append(int(random.uniform(0,100)))
    if(T[i]>max):
        max = T[i]
    if(T[i]<min):
        min = T[i]
   
T.append(-1)
print(min,max,len(T)-1)