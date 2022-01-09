# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 06/12/2021

Exercice n°3 du TD n°5
'''

'''
Dans le cadre d'un projet qui consiste à étiqueter d'un code-barre les ouvrages scolaires d'un établissement de 3 000 élèves,
prévoir un ou plusieurs dictionnaire(s) permettant de connaître les livres que possède chaque élève.
'''

import random

def generate_code(livre, nombre):
    code_barre = 100000
    dict_livre = {}
    for u in range(0, nombre):
        dict_livre[code_barre] = livre
        code_barre += 1
    return dict_livre

file = open("TD5_save.txt", 'w')

dict_eleve = {}

dict_histoire = generate_code("histoire", 3000)
dict_maths = generate_code("mathématiques", 3000)
dict_physique = generate_code("physique", 3000)
dict_svt = generate_code("SVT", 3000)
dict_anglais = generate_code("Anglais", 3000)
dict_espagnol = generate_code("espagnol", 3000)

dict_livre_name = {1 : "dict_histoire", 2: "dict_maths", 3: "dict_physique", 4: "dict_svt", 5: "dict_anglais", 6: "dict_espagnol"}

list_livres = ["none", "histoire", "mathématiques", "physique", "svt", "anglais", "espagnol"]
code_save = []

for i in range(1, 3001):
    nombre_de_livre = random.randint(1, 6)
    rand_livre = []

    for a in range(1, nombre_de_livre + 1):
        code_barre_aleatoire = random.randint(100000, 102999)
        if code_barre_aleatoire not in code_save:
            dictionnaire = dict_livre_name.get(a)

            rand_livre.append(eval(dictionnaire).get(code_barre_aleatoire))
            if a > 1:
                code_save.append(" livre " + list_livres[a] +  ' : ' + str(code_barre_aleatoire))
            else:
                code_save.append('éleve' + str(i) + " livre " + list_livres[a] +  ' : ' + str(code_barre_aleatoire))
        else:
            nombre_de_livre += 1
    dict_eleve[i] = rand_livre
    
file.write(str(code_save).replace(",", "\n"))
    
    

