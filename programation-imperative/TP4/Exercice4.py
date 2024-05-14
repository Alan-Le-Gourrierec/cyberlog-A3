import math

def Anniversaire(people):
    notprob = math.factorial(365)/(math.factorial(365-people)*365**people)
    return 1 - notprob

print(Anniversaire(23))