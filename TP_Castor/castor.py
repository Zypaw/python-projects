import csv
import math

# Pour ouvrir le csv
fichier = open("Castor2.csv")
table = list(csv.DictReader(fichier,delimiter=";"))
# Pour trier le csv en fonction de la note
table_nom = sorted(table, reverse=True, key=lambda item:str(item["Nom"]))
classement = sorted(table, reverse=True, key=lambda item:int(item["score"]))

##########
#   __   #  DEBUT
#  /_ |  #   name <- demander "Quel est votre nom de famille ?"
#   | |  #   Pour chaque i dans table:
#   | |  #       si name dans i["Nom"] alors
#   | |  #           afficher "{i['Nom']} {i['Prénom']} a eu {i['score']} points"
#   |_|  #       fin si
#        #  FIN
##########

def ex1():
    iteration = 0
    name = str(input("Quel est votre nom de famille ? (Ex:Bonduelle) \n--> "))
    for i in table:
        iteration += 1 # Pour compter le nombre d'opérations
        if name.lower() in i["Nom"].lower():
            print(f"{i['Nom']} {i['Prénom']} a eu {i['score']} points")
    print(f"Ce programme a fait {iteration} opérations\n")


##########  DEBUT
#  ___   #  name <- demander "Quel est votre nom de famille ?"
# |__ \  #  Pour chaque index de 0 à longueur(table):
#    ) | #      i <- table[index]
#   / /  #      si name dans i["Nom"] alors
#  / /_  #           afficher "{i['Nom']} {i['Prénom']} a eu {i['score']} points, vous êtes donc au {index+1} rang"
# |____| #           couper le programme ( ceci permet de rendre le coût plus faible en arrétant le programme lors de la trouvaille )
#        #      fin si
##########   FIN

def ex2():
    iteration = 0
    name = str(input("Quel est votre nom de famille ? (Ex:Bonduelle) \n--> "))
    for index in range(len(classement)):
        iteration += 1 # Pour compter le nombre d'opérations
        i = classement[index]
        if name.lower() in i["Nom"].lower():
            print(f"{i['Nom']} {i['Prénom']} a eu {i['score']} points, vous êtes donc au {index+1} rang")
            break
    print(f"Ce programme a fait {iteration} opérations\n")

########### 
#  ____   # 
# |___ \  # Le coût machine est important car nous devons parcourir toute les valeurs jusque trouver la bonne .
#   __) | # 
#  |__ <  #
#  ___) | # Nous pouvons faire une double recherche avec la méthode dichotomique qui aura donc un cout plus faible .
# |____/  # En cherchant d'abord son nombre de point puis sa place dans le classement
#         #
########### 

def ex3():
    name = str(input("Quel est votre nom de famille ? (Ex:Bonduelle) \n-->"))

    iteration=0
    # Ici on cherche la personne
    gauche = 0
    droite = len(table_nom)
    trouver = False
    while trouver != True:
        iteration += 1 # Pour compter le nombre d'opérations
        millieu = (gauche+droite)//2
        i = table_nom[millieu]
        if name.lower() in i["Nom"].lower():
            personne = i
            trouver = True
        elif name.lower() < i["Nom"].lower():
            gauche = millieu
        elif name.lower() > i["Nom"].lower():
            droite = millieu
        elif gauche == droite:
            print("Non trouvé")
            break
    if trouver == True:
        gauche = 0
        droite = len(classement)-1
        trouver = False
        while trouver != True:
            iteration += 1 # Pour compter le nombre d'opérations
            millieu = math.floor((gauche+droite)/2)
            i = classement[millieu]
            if int(personne["score"]) < int(i["score"]):
                gauche = millieu
            elif int(personne["score"]) > int(i["score"]):
                droite = millieu
            elif int(personne["score"]) == int(i["score"]):
                if personne["Nom"].lower() == i["Nom"].lower():
                    print(f"{i['Nom']} {i['Prénom']} a eu {i['score']} points, vous êtes donc au {millieu+1} rang")
                    trouver = True
                    break
                else:
                    for millieu in range(gauche,droite+1):
                        iteration += 1 # Pour compter le nombre d'opérations
                        i = classement[millieu]
                        if personne["Nom"].lower() == i["Nom"].lower():
                            print(f"{i['Nom']} {i['Prénom']} a eu {i['score']} points, vous êtes donc au {millieu+1} rang")
                            trouver = True
                            break
    print(f"Ce programme n'a fait que {iteration} opérations\n")
        
ex1()
ex2()
ex3()

# Suite à cette démonstration on peut en constater que la dichotomie est vraiment trés efficace pour reduire le coût nécessaire
