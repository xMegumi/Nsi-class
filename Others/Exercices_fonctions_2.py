# -*- coding: utf-8 -*-
'''
:Titre : Construction de fonctions
:Auteur : L. Conoir
:Date : 10/2019

Exercices : écrire les fonctions en vous basant sur le docstring établi
'''


##################################################################################
def change_joueur_ver2(joueur) :
    ''' La fonction retourne le nom du joueur suivant dans une partie à 2 joueurs

:param: joueur, type str, le nom du joueur actuel
:return: type str, 'joueur2' si le joueur actuel est 'joueur1', et vice-versa
:CU: joueur est une chaine de caractère
:bord_effect: None

:Examples:
>>> change_joueur_ver2('joueur1')
'joueur2'
>>> change_joueur_ver2('joueur2')
'joueur1'
    '''
    if joueur == 'joueur1':
        return 'joueur2'
    else:
        return 'joueur1'



##################################################################################
def change_joueur_ver3(joueur) :
    ''' La fonction retourne le nom du joueur suivant dans une partie à 3 joueurs

:param: joueur, type str, le nom du joueur actuel
:return: type str, 'joueur2' si le joueur actuel est 'joueur1',
                   'joueur3' si le joueur actuel est 'joueur2',
                   'joueur1' si le joueur actuel est 'joueur3',
:CU: joueur est une chaine de caractère
:bord_effect: None

:Examples:
>>> change_joueur_ver3('joueur1')
'joueur2'
>>> change_joueur_ver3('joueur2')
'joueur3'
>>> change_joueur_ver3('joueur3')
'joueur1'
    '''
    if joueur == 'joueur1':
        return 'joueur2'
    elif joueur == 'joueur2':
        return 'joueur3'
    else:
        return 'joueur1'



##################################################################################
def change_joueur_ver2bis(joueur,gagne) :
    ''' La fonction retourne le nom du joueur suivant dans une partie à 2 joueurs
        mais le joueur actuel rejoue si le coup quil vient de jouer est gagnant

:param: joueur, type str, le nom du joueur actuel
:param: gagne, type bool, True lorsque le joueur actuel a gagné, False s'il n'a pas gagné
:return: type str, nom du joueur qui doit jouer
:CU: joueur est une chaine de caractère, gagne est une variable boolénne
:bord_effect: None

:Examples:
>>> change_joueur_ver2bis('joueur1', True)
'joueur1'
>>> change_joueur_ver2bis('joueur1', False)
'joueur2'
>>> change_joueur_ver2bis('joueur2', True)
'joueur2'
>>> change_joueur_ver2bis('joueur2', False)
'joueur1'

    '''
    if joueur == 'joueur1' and gagne == True:
        return 'joueur1'
    elif joueur == 'joueur1' and gagne == False:
        return 'joueur2'
    elif joueur == 'joueur2' and gagne == True:
        return 'joueur2'
    else:
        return 'joueur1'




##################################################################################
################ procédure de tests pour les fonctions ###########################
##################################################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod()
