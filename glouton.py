from operator import index
import random

def generate_random_boxes(number):
    table = []
    for i in range(number):
        table.append({"size": random.randint(5, 10),
                     "price": random.randint(10, 30)})
    for i in range(len(table)):
        table[i]["average"] = table[i]["price"]/table[i]["size"]
    return table

# algorithme glouton (table,max_place):
#     i -> 0
#     camion -> un tableau
#     tant que max_place est plus grand que 0:
#         si i est égale à la longueur de la table:
#             fin de tant que
#         si la taille de l'object est plus petit que la taille restante(max_place):
#             ajout de l'object au tableau camion
#             on retire la taille de l'object a la taille restante (max_place)
#         on ajoute 1 à i pour incrémenter l'index
#     retourner le tableau camion

def remplir_camion(max_place, table):
    i = 0
    camion = []
    while(max_place>0):
        if i == len(table):
            break
        elif not (table[i]["size"] > max_place):
            camion.append(table[i])
            max_place -= table[i]["size"]
        i = i+1
    return camion

table = generate_random_boxes(10)
table = sorted(table, reverse=True, key=lambda item:item["average"])
print("Boîtes")
for i in table:
    print(i)
table = remplir_camion(40,table)
print("Camion :")
for i in table:
    print(i)