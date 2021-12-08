# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 08/11/2021

Exercice n°2 du TD n°3
'''

'''
Constituez un tableau semaine contenant les 7 jours de la semaine.
1. À partir de ce tableau, comment récupérez-vous seulement les 5 premiers jours de la semaine d'une part, et ceux du week-end d'autre part ? Utilisez pour cela l'indiçage. 
2. Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage).
3. Trouvez deux manières pour accéder au dernier jour de la semaine. 
4. Inversez les jours de la semaine en une commande.
'''

# 1
jours = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']

#2)
# Premier moyen
for i in range(0,7):
    if i < 5:
        print("jours de la semaine : ",jours[i])
    else:
        print("Week-end : ", jours[i])

print("-------------------------------")
#Deuxième moyen
for i in jours:
    if i != 'samedi' and i != "dimanche":
        print("Les jours de la semaine sont : ", i)
    else:
        print("Les jours du week_end sont : ", i)

print("-------------------------------")
# 3)
print("Dernier jour de la semaine : ",jours[-1])

print("-------------------------------")
t = len(jours) - 1
print("Dernier jour de la semaine : ",jours[t])

print("-------------------------------")
# 4)
jours.reverse()
print(jours)
