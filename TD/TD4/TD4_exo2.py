# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 02/12/2021

Exercice n°2 du TD n°4
'''
import doctest

def milieu(first_tuple, second_tuple):
    """  Documentation :
la fonction retourne un tuple formé des coordonnées du milieu des 2 points.
:param: first_tuple, second_tuple type tuple
:return: tuple
:CU: les arguments sont du type tuple

examples:
>>> milieu((5,3),(8,6))
(4, 7)
>>> milieu((2,10),(6,11))
(6, 8)
"""
    return ((first_tuple[0] + first_tuple[1]) //2, (second_tuple[0] + second_tuple[1]) // 2)

doctest.testmod(verbose=True)