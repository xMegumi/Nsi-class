# -*- coding: utf-8 -*-
'''
:Titre : TD1
:Auteur : Lorenzo
:Date : 15/09/2021

Exercice n°2 du TD n°1
'''

"""
Déclarer une variable joueur_actuel en y affectant la valeur 0.

Déclarer une variable nombre_tours en y affectant la valeur 10.
Un jeu se déroule en 10 tours de table, sous la direction d'un arbitre (utilisateur du programme).
A chaque tour, l'arbitre choisit le premier joueur (joueur1 ou joueur2) en donnant la valeur 1 ou 2.

En utilisant une boucle, faire afficher le déroulement d'une partie :
"""

joueur_actuel = 0
nombre_tours = 10

for i in range(nombre_tours):
    print("Tour n°", i+1)
    joueur_actuel = int(input("Quel est le premier joueur ? "))
    if joueur_actuel > 0 and joueur_actuel <= 2:
        print("C'est au joueur", joueur_actuel, "à jouer.")
    else:
        print("Joueur inexistant")
        break
    
print("fin de la partie.")
