# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 02/12/2021

Exercice n°1 du TD n°3
'''
import doctest

def suivants(entier):
    """ Documentation :
la fonction renvoie 1 tuple formé des 3 entiers suivants.
:param: entier, type int
:return: tuple
:CU: entier est du type int

examples:
>>> suivants(5)
(6, 7, 8)
>>> suivants(-8)
(-7, -6, -5)
    """
    return (entier + 1, entier + 2, entier + 3)

doctest.testmod(verbose=True)