a1 = 2
a2 = 0
a3 = 5
k = 3
seed = [1,0,3]
m = 10

for i in range(5):
    print(i + 1, " : ", seed) 
    tmp = a1 * seed[0] + a2*seed[1] + a3*seed[2]
    seed[0] = seed[1]
    seed[1] = seed[2]
    seed[2] = tmp % m
   
    