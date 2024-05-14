import datetime as dt
from math import floor

def Date():
    error = 1
    while(error == 1):
        #la fonction try permet dans ce cas si de vérifier si la date est sous le bon format 
        try:
            #normalement nous ne métons pas d'input dans les fonction mais ceci simplifias **BEAUCOUP** la chose
            jour,mois,annee= input("entrer la date (jour/mois/annee) :\n").split("/")
            jour,mois,annee = int(jour),int(mois),int(annee)
            error = 0
        except ValueError:
            print("Oups ! La valeur de la date n'est pas bonne ...")
            error = 1
    #les boucles suivantes vérifient si la date est bien conforme avec les condition des années bisextiles et donc la durée des mois 
    while(1 > mois or 12<mois):
        mois = int(input("donner un nouveau mois\n"))

    while(1900>annee or 2100<annee):
        annee = int(input("donner une nouvelle annee\n"))

    while(1>jour or 31<jour):
        jour = int(input("le jour est invalide ...\n"))
        
    while(mois == 2 and annee%4 == 0 and jour > 29):
        jour = int(input("donner une nouvelle jour\n"))

    while(mois == 2 and annee%4!=0 and jour>28):
        jour = int(input("donner une nouvelle jour\n"))

    while(mois == {4,6,9,11} and jour >30): 
        jour = int(input("donner une nouvelle jour\n"))
        
    return jour,mois,annee

def Lendemain(jour,mois,annee):
    #même principe que la fonction date mais avec des if
    if mois == 2 :
        if annee%4 == 0 and jour == 29:
            mois+=1
            jour=1
        elif annee%4!=0 and jour == 28:
            mois+=1
            jour=1
        else:
            jour+=1
    elif mois == {4,6,9,11} and jour == 30:
        mois+=1
        jour=1
    
    elif mois == 12 and jour == 31:
        jour,mois = 1,1
        annee+=1
    elif jour == 31:
        mois+=1
        jour =1
    else:
        jour+=1
    return jour,mois,annee

def Temps(jour,mois,annee):
    #permet de savoir le nombre de jour dans une depuis l'an 0 (utilisé dans des fonction comme NextDate et Age)
    if mois == 2:
        jour+=59
        if annee%4 == 0:
            jour+=1
    jour+=floor(annee*355.25)
    return jour
    
def NextDate(t1,t2):
    #elle fais juste la différence entre deux date pour connaître leur écarts
    return abs(t1-t2)

def Age(jn,mn,an):
    #donne l'âge en année de l'utilisateur
    tj,tm,ta = dt.date.today().strftime("%d/%m/%Y").split("/")
    tj,tm,ta = int(tj),int(ta),int(ta)
    t1,t2 = Temps(jn,mn,an),Temps(tj,tm,ta)
    
    if(t1>t2):return "la date de naissance est invalide ou vous êtes née dans longtemps"
    else: return (t2-t1)//365

date1,date2 = None,None 
print("voici les choix:\n a. entrer une date (limité à 2)\n donner le lendemain d'une des dates\n c. Donner le temps entre les deux dates\n d. Vôtre age\nq. Quiter (choix par defaut)")

while True:
    #menu qui permet de résoudre les potentiels problème (auquelle j'ai pensé) que l'utilisateur pourrais rencontrer si il lance mal les divers fonctions
    menu = input("entrer l'option de votre choix (m. affiche le menu\n")
    match menu:
        case "a":
            if date1 == None:
                j1,m1,a1 = Date()
            elif date2 == None:
                j2,m2,a2 = Date()
            else:
                tmp = int(input("quelle date voulez vous changer :\n 1.remplacer la date 1 (choix par defaut)\n2.remplacer al date 2"))
                match tmp :
                    case 2:
                        j2,m2,a2 = Date()
                    case _:
                        j1,m1,a1 = Date()
        case "b":
            tmp = int(input("de quelle date :\n 1. date 1 (chois par defaut)\n2. date 2\n"))
            match tmp:
                case 2:
                    if date2 == None:j2,m2,a2 = Date(date2)
                    print(Lendemain(j2,m2,a2))
                case _:
                    if date1 == None:j1,m1,a1 = Date(date1)
                    print(Lendemain(j1,m1,a1))
        case "c":
            if date1 == None:
                date1=input("la date 1 n'existe pas, entrer une nouvelle date :\n")
                j1,m1,a1 = Date(date1) 
            if date2 == None:
                date2=input("la date 2 n'existe pas, entrer une nouvelle date :\n")
                j2,m2,a2 = Date(date2)
            print("il y à : ",NextDate(Temps(j1,m1,a1),Temps(j2,m2,a2)),"jours de diférences")
        case "d":
            print("quelle jour êtes vous née :\n")
            jn,mn,an = Date()
            print("vous avez :", Age(jn,mn,an),"ans")
            
        case "m":
            print("voici les choix:\n a. entrer une date (limité à 2)\n donner le lendemain d'une des dates\n c. Donner le temps entre les deux dates\n d. Vôtre age\nq. Quiter (choix par defaut)")    
        case _:
            break