# -*- coding: utf-8 -*-
'''
:Titre : TD Codage en génétique
:Auteur : Lorenzo
:Date :  11.03.2022

Exercices du TD n°8
'''
import doctest

# a)
def chiffrement_cesar(value, key):
    """La fonction retourne le chiffrement de cette chaîne par l'encodage
Cesar avec la clé de chiffrement fournie en paramètre.

examples:
>>> chiffrement_cesar('INFORMATIQUE',3)
'LQIRUPDWLTXH'
>>> chiffrement_cesar('Cesar vs Turing',10)
'MOCKB FC DEBSXQ'
>>> chiffrement_cesar('LQIRUPDWLTXH',-3)
'INFORMATIQUE'
"""
    output = ""
    for i in value.upper():
        if i == " ":
            output += " "
        else:
            output += chr(65 + (ord(i) - 65 + key) % 26)
    return output


# b)
print(chiffrement_cesar("ebqoxd ovswsxob vk mslvo", -10))

# c)
def casse_cle_cesar(text_clear, text_chiffre):
    """la fonction retourne la clée entre le texte clair et le texte
chiffré.

Examples:
>>> casse_cle_cesar("rendez vous rue de la paix", "mziyzu qjpn mpz yz gv kvds")
21
"""
    for i in range(0,26):
        cesar = chiffrement_cesar(text_chiffre.upper(), -i)
        if cesar == text_clear.upper():
            return i
        
# d)
def cesar_mot(text, mot):
    """La fonction cherche la clé et le message decripté à
partir d'un mot connu.
Examples:
>>> cesar_mot('stywj jssjrn ij ytzotzwx jxy ij wjytzw', "ennemi")
('NOTRE ENNEMI DE TOUJOURS EST DE RETOUR', 5)
"""
    for i in range (0,26):
        code = chiffrement_cesar(text, -i)
        if mot.upper() in code:
            return code, i

# e)
# Le mot est 'ENQUETE' est sa clé est '22'
for i in range(0,26):
    code = chiffrement_cesar('AJMQAPA', -i)
    print(code, i)

doctest.testmod(verbose = True)