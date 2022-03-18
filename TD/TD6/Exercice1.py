# -*- coding: utf-8 -*-
'''
:Titre : Création d'une table de données
:Auteur : 
:Date : 05/2020

Exercice n°1 du TD n°8
'''


##################################################################################################################
## Question a)
##################################################################################################################
with open("support/personnes.csv", 'r', encoding = 'UTF-8') as fichier :    # ouverture du fichier en mode lecture
    lignes = fichier.readlines()                     # lire les lignes
    
descripteurs = lignes[0].strip("\n").rsplit(",") # prendre la première ligne en enlevant le retour à la ligne et en séparant les descripteurs

donnees = []                       # liste contenant les enregistrements (données des lignes suivantes)

for ligne in lignes[1:] :                          # pour chaque ligne suivante
   donnees.append(ligne.rstrip("\n").split(","))
                                                   # à vous de continuer




##################################################################################################################
## Question b)
##################################################################################################################
def correction_majuscules() :
    '''La fonction vérifie et corrige la majuscule de chaque nom et prénom dans la variable 'donnees'.

:param: None
:return: None
:CU: la variable 'donnees' existe, une liste de listes
:bord_effect: la valeur de la variable 'donnees' peut être modifiée
'''
    majuscule = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R","S", "T","U", "V", "W", "X", "Y","Z"]
    count = 0
    for value in donnees:
        nom = value[0]
        prenom = value[1]
        if not nom[0] in majuscule or not prenom[0] in majuscule:
            nom = nom.capitalize()
            prenom = prenom.capitalize()
            
            donnees[count] = [nom, prenom, value[2]]
        count += 1


##################################################################################################################
## Question c)
##################################################################################################################
def doublons() :
    '''La fonction élimine de la variable 'donnees' les enregistrements en double.

:param: None
:return: None
:CU: la variable 'donnees' existe, une liste de listes
:bord_effect: la valeur de la variable 'donnees' peut être modifiée
'''
    supp = []
    for value1 in range(len(donnees) - 1):
        for value2 in range(value1 + 1, len(donnees)):
            if donnees[value1] == donnees[value2]:
                supp.append(value2)
    
    supp.reverse()
    print(supp)
    for indice in supp:
        del donnees[indice]
                

"""
##################################################################################################################
## Question d)
##################################################################################################################
def tri_age() :
    '''La fonction ordonne les enregistrements de la variable 'donnees' par age décroissant.

:param: None
:return: None
:CU: la variable 'donnees' existe, une liste de listes
:bord_effect: la valeur de la variable 'donnees' peut être modifiée
'''
    pass   # à effacer

    
##################################################################################################################
## Question e)
##################################################################################################################
"""