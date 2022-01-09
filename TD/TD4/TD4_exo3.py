# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 02/12/2021

Exercice n°3 du TD n°4
'''

import doctest

def maximums(tuple1):
    """ Documentation :
la fonction retourne les 2 plus grands nombres sous forme de tuple.
:param: tuple, type tuple
:return: tuple
:CU: L'argement doit être un tuple

examples:
>>> maximums((5, 6, 7))
(6, 7)
>>> maximums((-10, -3, -6))
(-3, -6)
"""
    return (max(tuple1[0], tuple1[1]), max(min(tuple1[0], tuple1[1]), tuple1[2]))

        

doctest.testmod(verbose=True)