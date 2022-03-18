# -*- coding: utf-8 -*-
'''
:Titre : TP Codage en génétique
:Auteur : 
:Date : 

Fonctions du TP n°6
'''
import random

def get_key(val, my_dict):
    '''
    Renvoie la key d'un dictionnaire à partir de sa valeur
'''
    for key, value in my_dict.items():
         if val == value:
             return key
            
##################################################################################################################
## Question 1
##################################################################################################################
def estADN(chaine) : 
    ''' Vérifie si la chaine mise en paramètre est une séquence ADN

:param chaine, type str, chaine de caractères
:return : type boolean, True si la chaine ne contient que des bases A, C, G ou T
:CU: chaine est de type str

:examples:
>>> estADN('ATGCGATC')
True
>>> estADN('ACKT')
False
>>> estADN('ACTK')
False
>>> estADN('')
True
    '''
    adn = ["A", "C", "G", "T"]
    for i in chaine:
        if not i in adn:
            return False
    return True

##################################################################################################################
## Question 2
##################################################################################################################
def genereADN(taille) : 
    ''' La fonction renvoie une séquence ADN, de longueur 'taille', générée de façon aléatoire.

:param: taille, type int, taille de la séquence souhaitée
:return: type str, séquence ADN de longueur 'taille'
:CU: taille >= 0

:examples:
>>> genereADN(0)
''
    '''
    adn = ["A", "C", "G", "T"]
    value = []
    for i in range(0,taille):
        value.append(random.choice(adn))
    return "".join(value)



##################################################################################################################
## Question 3
##################################################################################################################
def baseComplementaire(base, sequence) : 
    ''' La fonction renvoie la base complémentaire de la 'base' passée en paramètre, suivant la 'sequence' définie.

:param: base, type str, base à tranformer
:param: sequence, type str, séquence ADN ou ARN
:return : type str, base complémentaire de 'base'
:CU: base est de str à un seul caractère, chaine n'admet que 2 valeurs ('ADN' ou 'ARN')

:examples:
>>> baseComplementaire('G', 'ADN')
'C'
>>> baseComplementaire('A', 'ARN')
'U'
    '''
    dict_ADN_ARN = {"A" : "U", "T" : "A", "G" : "C", "C" : "G"}
    
    if sequence == 'ADN':
        value = get_key(base, dict_ADN_ARN)
    elif sequence == 'ARN':
        value = dict_ADN_ARN.get(base)
    else:
        print("erreur")
    return value
    
    
        
       

##################################################################################################################
## Question 4
##################################################################################################################
def transcrit(chaine, indice_1, indice_2) : 
    '''La fonction renvoie l'ARN construit à partir de la sous-séquence d'ADN 'chaine',
comprise entre les deux positions, 'indice_1' et 'indice_2'

:param chaine, type str, séquence ADN
:param indice_1, type int, position de début dans 'chaine' (la numérotation commence à 1)
:param indice_2, type int, position de fin dans 'chaine'
:return: type str, séquence ARN
:CU: 'chaine' est une séquence ADN, indice_1 et indice_2 sont des entiers non nuls

:examples:
>>> transcrit('TTCTTCTTCGTACTTTGTGCTGGCCTCCACACGATAATCC', 1, 4)
'AAGA'
>>> transcrit('TTCTTCTTCGTACTTTGTGCTGGCCTCCACACGATAATCC', 4, 23)
'AAGAAGCAUGAAACACGACC'
    '''
    
    chaine = list(chaine)
    values = []
    for i in range(1, len(chaine)):
        if indice_1 <= indice_2:
            values.append(baseComplementaire(chaine[indice_1], 'ADN'))
            print(chaine[indice_1])
            print(baseComplementaire(chaine[indice_1], 'ADN'))
            indice_1 += 1
    return "".join(values)

"""
##################################################################################################################
## Question 5
##################################################################################################################
def codeGenetique(codon) :
    '''La fonction codeGenetique renvoie l'acide aminé (sous la forme du nom abrévié EN 1 lettre)
correspondant au codon passé en paramètre, ou pour les codons Stop.

:param codon, type str, séquence de 3 bases
:return: type str, acide aminé
:CU: 'codon' est de type str
    '''
    
    pass


##################################################################################################################
## Question 6
##################################################################################################################
def traduit(chaine) :
    '''La fonction renvoie la séquence protéique obtenue par la traduction de la séquence ARN passée en paramètre.

:param chaine, type str, séquence de longueur multiple de 3
:return: type str, suite d'acides aminés
:CU: 'chaine' est de type str

:examples:
>>> traduit('AAUUCAAUUUAA')
'NSI*'
>>> traduit('AUGCGAAGCCGAAAGAACACCGGCUAA')
'MRSRKNTG*'
    '''

    pass


##################################################################################################################
## Question 7
##################################################################################################################
def replique(chaine) :
    ''' La fonction renvoie la séquence ADN complémentaire à celle passée en paramètre, en l'inversant.

:param chaine, type str, séquence d'ADN
:return: type str, séquence d'ADN
:CU: 'chaine' est de type str et correspond à une séquence ADN

:examples:
>>> replique('ACTG')
'CAGT'
    '''
    
    pass


##################################################################################################################
## Menu
##################################################################################################################
def menu() :
    pass
    
##################################################################################
################ procédure de tests pour les fonctions ###########################
##################################################################################
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)