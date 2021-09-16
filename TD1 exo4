# -*- coding: utf-8 -*-
'''
:Titre : TD1
:Auteur : Lorenzo 
:Date : 15/09/2021

Exercice n°4 du TD n°1
'''
texte = "Les licences de droits d’auteur et les outils Creative Commons apportent un équilibre à l’intérieur du cadre traditionnel “tous droits réservés” créé par les lois sur le droit d’auteur. Nos outils donnent à tout le monde, du créateur individuel aux grandes entreprises et aux institutions publiques, des moyens simples standardisés d’accorder des permissions de droits d’auteur supplémentaires à leurs œuvres. La combinaison de nos outils et de nos utilisateurs est un fonds commun numérique vaste et en expansion, un espace commun de contenus pouvant être copiés, distribués, modifiés, remixés, et adaptés, le tout dans le cadre des lois sur le droit d’auteur."

# questions

'''
Écrire un programme permettant de compter les lettres 'a' dans ce texte.

Écrire un programme permettant de compter les voyelles dans ce texte.

Écrire un programme qui affiche ce texte après avoir échangé les lettres 'a' et 'e' , 'i' et 'o'
'''

# Question 1
nb_a = 0

for i in texte:
    if i == 'a' or i == 'A':
        nb_a += 1
print(f'{nb_a} a trouvées')

# Question 2 
nb_v = 0
ls_v = ["a","e", "i", "o", "u","y"]

for letter in texte:
    for i in ls_v:
        if letter == i:
         nb_v += 1
print(f"{nb_v} de voyelles trouvées")

# Question 3
data_dictonary = {'a': 'e', 'e': 'a', 'i': 'o', 'o': 'i'}
texte_m = ""

for i in texte:
    if i in data_dictonary:
        texte_m += data_dictonary[i]
    else:
        texte_m += i
print(texte_m)
           
