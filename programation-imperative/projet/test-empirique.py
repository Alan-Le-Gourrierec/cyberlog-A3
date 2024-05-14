import ultraMastermind as master
import time
import random
import matplotlib.pyplot as plt
import math 

def EvalutaionEmpirique(taille_pop,mutation_rate,taux_conservation,size):
    iteration,moy = 50,20
    quantite=10 #permetras d'obtenir une moyenne afin d'améliorer le graph finale
    values = []
    
    labels = [x for x in range(iteration)]
    for i in range(iteration):
        tmp = [Genetique(taille_pop,mutation_rate,taux_conservation,i) for _ in range(moy)]
        values.append(sum(tmp)/moy)
    plt.plot(labels, values)
    plt.xlabel = "nombre d'itérations"
    plt.ylabel = "time"
    plt.show()

def Genetique(taille_pop, taux_mutation, taux_conservation, size):
    t = time.time()
    generation = 0
    mot_de_pass = master.Proposition(size)

    pop = master.Population(taille_pop, size)

    while True:  
        eval = master.FitnessPop(mot_de_pass, pop)
        if mot_de_pass in pop:
            return time.time() -t
            #return generation +1

        parents = master.Eugenisme(pop, eval, taux_conservation)
        enfants = [master.Mutation(master.Reproduction(parents, size), taux_mutation) for _ in range(taille_pop - len(parents))]

        generation += 1
        pop = parents + enfants

        pop.sort(key=lambda x: master.Fitness(mot_de_pass, x)[0], reverse=True)

if __name__ == "__main__":
    taille_pop = 100
    mutation_rate = 0.05
    size = 20
    taux_conservation = 0.5

    EvalutaionEmpirique(taille_pop,mutation_rate,taux_conservation,size)
