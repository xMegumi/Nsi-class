# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 06/12/2021

Exercice n°1 du TD n°5
'''

d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

'''
1. Ecrire une instruction pour corriger l'erreur dans le prénom, la bonne valeur est 'Jacques'. 
2. Afficher la liste des clés du dictionnaire. 
3. Afficher la liste des valeurs du dictionnaire. 
4. Afficher la liste des paires clé/valeur du dictionnaire. 
5. Ecrire la phrase "Jacques Dupuis a 30 ans".
'''

# Question 1
d['prenom'] = "Jacques"

# Question 2
print(d.keys())

# Question 3
print(d.values())

# Question 4

print(d.items())

# Question 5
print(d.get('prenom'), d.get('nom'), "a", d.get('age'), 'ans')
