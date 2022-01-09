# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 02/12/2021

Exercice n°4 du TD n°4
'''

import doctest

def moyenne(notes):
    """ Documentation :
la fonction retourne la moyenne des notes entrées.
:param: notes, type tuple
:return: float or int
:CU: Les arguments sont du type tuple de valeur int

examples:
>>> moyenne((10,15,16))
13.67
>>> moyenne((18.5, 13.2, 18))
16.57
"""
    return round(sum(notes) / len(notes), 2)

doctest.testmod(verbose=True)