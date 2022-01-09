# -*- coding: utf-8 -*-
'''
:Titre : Construction de fonctions
:Auteur : Lorenzo
:Date : 10/2021

Consigne : compléter les fonctions en vous basant sur le docstring établi
        ou écrire le docstring lorsq'il n'est pas présent en analysant la fonction
'''
import math

##################################################################################
def premier(n) :
    ''' Cette fonction précise si le nombre n est un nombre premier
        Un nombre premier est un nombre seulement divisible par 1 et par lui-même.
        On considère que 1 n'est pas un nombre premier

:param: n, type int, un nombre entier
:return: type bool, True si n est un nombre premier, False dans l'autre cas
:CU: n est un nombre entier positif
:bord_effect: None

:Examples:
>>> premier(17)
True
>>> premier(15)
False
>>> premier(1)
False
    '''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
                                                   
##################################################################################
def premier_suivant(rang) :
    ''' Cette fonction ... 

:param:
:return:
:CU:
:bord_effect:

:Examples:
>>> premier_suivant(3)
5
>>> premier_suivant(20)
23
>>> premier_suivant(32)
37
    '''
# partie à décommenter lorsque la fonction premier() est écrite
#    nombre = rang + 1                 
#    
#    while not premier(nombre) :       
#        nombre = nombre + 1           
#    
#    return nombre
    nombre = rang + 1
    
    while nombre != premier(nombre):
        nombre = nombre + 1
    return nombre



##################################################################################
def cle_numero_secu(n_secu_sans_cle) :
    ''' Cette fonction calcule la clé de contrôle du numéro de sécurité sociale
        puis l'ajoute à la fin du numéro fourni.
        
:param: n_secu_sans_cle, type int, un numero de sécurité sociale à 13 chiffres
:return: type int, clé à 2 chiffres calculée à partir de n_secu
:CU: n est un nombre entier positif à 13 chiffres, commençant par 1 ou 2
:bord_effect: None

:Examples:
>>> cle_numero_secu(1021262193561)
102126219356170
>>> cle_numero_secu(2030759318247)
203075931824728
    '''
    cle = 97 - (n_secu_sans_cle % 97)       # definition officielle de la clé
    return n_secu_sans_cle * 100 + cle                              # clé ajoutée à la fin du numéro de sécurité sociale



##################################################################################
def verif_numero_secu(n_secu_avec_cle) :
    ''' Cette fonction vérifie si le numéro de sécurité sociale est valide

:param: n_secu_avec_cle, type int, un numero de sécurité sociale à 13 chiffres
:return: type int, clé à 2 chiffres calculée à partir de n_secu
:CU: n est un nombre entier positif à 15 chiffres, commençant par 1 ou 2
:bord_effect: None

:Examples:
>>> verif_numero_secu(102126219356170)
True
>>> verif_numero_secu(203075931824725)
False
    '''
    r = n_secu_avec_cle % 100
    return (n_secu_avec_cle - r) // 100
    
    
    
##################################################################################
################ procédure de tests pour les fonctions ###########################
##################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
