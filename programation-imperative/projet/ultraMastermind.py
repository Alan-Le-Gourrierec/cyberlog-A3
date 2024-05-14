import random
import time

def Proposition(size):
    return [random.randint(0, 255) for _ in range(size)]

def Population(taille_pop, size):
    return [Proposition(size) for _ in range(taille_pop)]

def Fitness(mot_de_pass, proposition):
    GP = BP = 0  # GP est good_position et BP est bad_position
    for i in range(min(len(mot_de_pass), len(proposition))):
        if mot_de_pass[i] == proposition[i]:
            GP += 1
        elif proposition[i] in mot_de_pass:
            BP += 1
    return GP, BP

def Eugenisme(population, evaluations, taux_conservation):
    taille_conserver = int(len(population) * taux_conservation)
    trie = [i for _, i in sorted(zip(evaluations, population), key=lambda couple: couple[0], reverse=True)]
    return trie[:taille_conserver]

def FitnessPop(mot_de_pass, population):
    return [Fitness(mot_de_pass, proposition) for proposition in population]

def Mutation(enfant, taux_mutation):
    for i in range(len(enfant)):
        if random.random() < taux_mutation:
            enfant[i] = random.randint(0, 255)
    return enfant

def Reproduction(parents, size):
    cut_point = random.randint(0, size)
    return parents[0][:cut_point] + parents[1][cut_point:]

def Genetique(taille_pop, taux_mutation, taux_conservation, size):
    t = time.time()
    generation = 0
    mot_de_pass = Proposition(size)
    print(f"Le code est : {mot_de_pass}\n")

    pop = Population(taille_pop, size)

    while True:  
        eval = FitnessPop(mot_de_pass, pop)
        if mot_de_pass in pop:
            print(f"Trouvé au bout de la {generation + 1}ème génération")
            print(pop[len(pop)-1])
            #return time.time() -t
            #return generation +1
            break

        parents = Eugenisme(pop, eval, taux_conservation)
        enfants = [Mutation(Reproduction(parents, size), taux_mutation) for _ in range(taille_pop - len(parents))]

        generation += 1
        pop = parents + enfants

        pop.sort(key=lambda x: Fitness(mot_de_pass, x)[0], reverse=True)