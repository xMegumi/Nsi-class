# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 06/12/2021

Exercice n°2 du TD n°5
'''

'''
Créer une fonction 'occurrence' qui prend en paramètre un texte et qui retourne un dictionnaire précisant le nombre d’occurrences
de chaque caractère dans le texte.
'''

def occurrence(texte):
    """ Documentation :
la fonction renvoie le nombre d'occurences de chaque caractère
dans le texte.
:param: texte, type str
:return: dict
:CU: L'argument doit être un texte

examples:
>>> occurrence("J'aime les fruits")
{'J': 1, "'": 1, 'a': 1, 'i': 2, 'm': 1, 'e': 2, ' ': 2, 'l': 1, 's': 2, 'f': 1, 'r': 1, 'u': 1, 't': 1}
>>> occurrence("pomme")
{'p': 1, 'o': 1, 'm': 2, 'e': 1}
"""
    characters_dict = {}
    for characters in texte:
        if characters in characters_dict:
            characters_dict[characters] += 1
        else:
            characters_dict[characters] = 1
    return characters_dict
        
        