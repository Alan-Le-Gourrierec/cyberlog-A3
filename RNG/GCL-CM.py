a= 1
b= 2
m= 3
seed= 1

for i in range(10):
    print(i," : ",seed)
    seed = (a*seed+b)%m