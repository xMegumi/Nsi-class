# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 08/11/2021

Exercice n°3 du TD n°3
'''

'''
1) Écrire une fonction repas(jour), qui demande à l’utilisateur le repas du jour précisé en paramètre et le renvoie.
2) A partir du tableau semaine de l’exercice 3 et de la fonction précédente, établir le tableau  repas_semaine contenant les repas de l’utilisateur pour tous les jours de la semaine.
'''

def repas(jour):
    plat = input("Quel repas voulez-vous pour " + jour + " : ")
    return plat

repas_semaine = []
jours = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']

for i in jours:
    repas_semaine.append(repas(i))

print(repas_semaine)
