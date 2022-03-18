# -*- coding: utf-8 -*-
'''
:Titre : 2- Le chiffre Atbash
:Auteur : Lorenzo
:Date :  18.03.2022

Exercices du TD n°8
'''
import doctest

def chiffrement_atbash(text):
    ''' La fonction renvoie le déchiffrage du texte avec la
méthode atbash.
Examples:
>>> chiffrement_atbash('HFXXVHH')
'SUCCESS'
'''
    output = ""
    bash = {'A' : 25, 'B' : 24, 'C' : 23, 'D' : 22, 'E' : 21, 'F' : 20, 'G' : 19, 'H' : 18, 'I' : 17, 'J' : 16,'K' : 15, 'L' : 14, 'M' : 13, 'N' : 12, 'O' : 11, 'P' : 10, 'Q' : 9, 'R' : 8, 'S' : 7, 'T' : 6, 'U' : 5, 'V' : 4, 'W' : 3,'X' : 2, 'Y' : 1, 'Z' : 0} 
    for i in text.upper(): 
        if i == " ":
            output += " "
        else:
            output += chr(65 + bash[i])
    return output

doctest.testmod()
