# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 08/11/2021

Exercice n°5 du TD n°3
'''

'''
Établir un programme qui partage aléatoirement un jeu de 32 cartes en 4 joueurs.

Aide : 
import random   (fonction random.choice())
couleur = ['Trefle', 'Carreau', 'Coeur', 'Pique']
valeur = ['7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
'''

import random

couleur = ['Trefle', 'Carreau', 'Coeur', 'Pique']
valeur = ['7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
jeu_de_cartes = []
joueur_1 = []
joueur_2 = []
joueur_3 = []
joueur_4 = []

for i in couleur:
    for y in valeur:
        jeu_de_cartes.append(y + i)
        
for i in range(0,4):
    for j in range(0,8):
        carte = random.choice(jeu_de_cartes)
        if i == 0:
            joueur_1.append(carte)
            jeu_de_cartes.remove(carte)
        elif i == 1:
            joueur_2.append(carte)
            jeu_de_cartes.remove(carte)
        elif i == 2:
            joueur_3.append(carte)
            jeu_de_cartes.remove(carte)
        elif i == 3:
            joueur_4.append(carte)
            jeu_de_cartes.remove(carte)
    
jeu = [joueur_1, joueur_2, joueur_3, joueur_4]
print("Carte du joueur 1 :",jeu[0][:])
print("Carte du joueur 2 :",jeu[1][:])
print("Carte du joueur 3 :",jeu[2][:])
print("Carte du joueur 4 :",jeu[3][:])
