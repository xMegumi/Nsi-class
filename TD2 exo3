# -*- coding: utf-8 -*-
'''
:Titre : Opérateurs et expressions booléennes
:Auteur : Lorenzo
:Date : 20/09/2021

Exercice n°3 du TD n°2
'''

"""
Exercice 3 : Nombre de jours depuis le début de l'année

Déclarer la date d'aujourd'hui en utilisant les variables jour, mois, annee, de type int().

Vérifier si l'année est bissextile et déclarer une variable booléenne est_bissextile dont la valeur précise si c'est le cas.

Déclarer une variable nb_jours_debut, initialisée à 0, qui permettra d'accumuler les jours comptés.

A l'aide d'une boucle for, passer en revue tous les mois entiers depuis le début de l'année et jusqu'au mois précédent. Ajouter au fur et à mesure le nombre de jours, en tenant compte de chaque mois.

Finir de compter avec le mois actuel et afficher alors le nombre de jours écoulés depuis le début de l'année.
"""

jour, mois, annee = int(input("jour : ")), int(input("mois : ")), int(input("annee : "))
est_bissextile = False
nb_jours_debut = 0

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

# Réponse
print(nb_jours_debut, "jours se sont écoulés depuis le début de l'année.")
