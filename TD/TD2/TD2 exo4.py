# -*- coding: utf-8 -*-
'''
:Titre : Opérateurs et expressions booléennes
:Auteur : Lorenzo
:Date : 30/09/2021

Exercice n°4 du TD n°2
'''

"""
Exercice 4 : Nombre de jours jusqu'à la fin de l'année

En vous inspirant de l'exercice précédent,
réaliser un programme déterminant le nombre restant avant la fin de l'année, que l'on affectera à la variable nb_jours_fin.
"""

jour, mois, annee = int(input("jour : ")), int(input("mois : ")), int(input("annee : "))
est_bissextile = False
nb_jours_debut = 0
nb_jours_fin = 0

# Je vérifie si l'année est bissextile.
if annee%4 == 0:
    if annee%100 == 0:
        if annee%400 == 0:
            est_bissextile = True
    else:
        est_bissextile = True

# Dictionnaire avec tout les mois
month_dictionary = {"janvier" : 31, "fevrier" : 28, "mars": 31, "avril": 30, "mai": 31, "juin": 30, "juillet": 31, "aout": 31, "septembre": 30, "octobre": 31, "novembre": 30, "decembre": 31}

# Si l'année est bissextile je change la valeur de fevrier en 29 jours.
if est_bissextile == True:
    month_dictionary.update({"fevrier": 29})

# Je retire 1 mois et j'ajoute le nombre de jours du mois.
mois -= 1
nb_jours_debut += jour

# Boucle des mois.
for key, value in month_dictionary.items():
    if mois > 0:
        nb_jours_debut += value
        mois -= 1
    else:
        break

# Réponse (Changer pour afficher les jours restant)
if est_bissextile == True:
    annee_f = 366
    nb_jours_fin = annee_f - nb_jours_debut
elif est_bissextile == False:
    annee_f = 365
    nb_jours_fin = annee_f - nb_jours_debut

print("Il reste", nb_jours_fin, "jours avant la fin de l'année.")
