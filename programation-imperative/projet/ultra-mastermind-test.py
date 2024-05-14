import ultraMastermind as master


if __name__ == "__main__":
    taille_pop = 100
    mutation_rate = 0.05
    size = 20
    taux_conservation = 0.5

    master.Genetique(taille_pop,mutation_rate,taux_conservation,size)