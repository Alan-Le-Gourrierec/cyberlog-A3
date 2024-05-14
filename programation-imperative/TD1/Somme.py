# Alan Le Gourrierec; TP : programation impérative; 13 septembre 2023

def SumArray(Table_somme):
    sum,i = 0,0
    while(i <= len(Table_somme)): # n est la longuer du tableau => n = len(A)
        sum = sum + Table_somme[i]
        i = i+1
    return sum

Table = [1,2,3,4,5,6,7,8,9]
print(SumArray(Table))