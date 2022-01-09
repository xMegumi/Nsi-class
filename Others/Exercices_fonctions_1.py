# -*- coding: utf-8 -*-
'''
:Titre : Construction de fonctions
:Auteur : L. Conoir
:Date : 10/2021

Consigne : compléter les fonctions en vous basant sur le docstring établi
        ou écrire le docstring lorsq'il n'est pas présent en analysant la fonction
'''


##################################################################################
def mediane(a,b) :
    ''' Cette fonction détermine la valeur médiane entre a et b

:param : a,b, type int, 2 nombres
:return: type float, médiane entre les nombres a et b
:CU: a et b sont deux nombres de types int
:bord_effect: None
:Examples:

>>> mediane(2,4)
3.0
>>> mediane(-2,5)
1.5
>>> mediane(3,3)
3.0
    '''
    return  (a+b)/2                 # formule


##################################################################################
def distance(a,b) :
    ''' Cette fonction détermine la distance entre a et b

:param : a,b, type int, 2 nombres
:return: type int, distance entre les nombres a et b
:CU: a et b sont deux nombres de types int
:bord_effect: None

:Examples:
>>> distance(1,7)
6
>>> distance(-2,5)
7
>>> distance(7,7)
0
    '''
    return (b-a)                # formule


##################################################################################
def p_rect(L,l) :
    ''' Cette fonction détermine le périmètre d'un rectangle de dimensions L,l

:param : L,l, type float, la longueur et la largeur respectives du rectangle
:return: type float, perimetre = 2 * (L + l)
:CU: L et l sont des nombres positifs, non nuls
:bord_effect: None

:Examples:
>>> p_rect(12,7)
38
>>> p_rect(10.5,5.2)
31.4
    '''
    return 2 * (L + l)      # formule


    
##################################################################################
################ procédure de tests pour les fonctions ###########################
##################################################################################
# décommenter les lignes suivantes
# chaque exemple écrit dans les docstrings des fonctions seront alors testés
# si rien n'est mentionné, les tests sont réussis

if __name__ == "__main__":
   import doctest
   doctest.testmod()
