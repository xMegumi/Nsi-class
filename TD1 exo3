# -*- coding: utf-8 -*-
'''
:Titre : TD1
:Auteur : Lorenzo
:Date : 15/09/2021

Exercice n°3 du TD n°1
'''

'''
Compléter le module identite.py afin de collecter les informations suivantes :

date de naissance : jour, mois, année
lieu de naissance : ville
adresse : numéro, voie, code postal, ville
Écrire ensuite une structure conditionnelle utilisant la date de naissance et la date d'aujourd'hui, afin de définir l'âge de la personne. Une variable age sera créée dans ce cas.

Faire afficher le texte suivant, en y insérant automatiquement les données collectées à la place des mots écrits en italique :

Je soussigné, Monsieur ou Madame (à préciser) nom prénom, né(e) le date de naissance à ville, demeurant adresse, certifie sur l'honneur l'exactitude des renseignements déclarés.
Fait le date d'aujourd'hui
'''
import datetime 

# importation du module identite.py
nom = input("Quel est votre nom ? ")
prenom = input("quel est votre prénom ? ")
sexe = input("Quel votre sexe (M ou F) ? ")

#date de naissance, adresse et lieu de naissance
jour, mois, annee = int(input("jour de naissance : ")), int(input("mois de naissance : ")), int(input("annee de naissance : "))
date_de_naissance = str(jour) + str(mois) + str(annee)
lieu_de_naissance = input("Quel est votre lieu de naissance ? ")
adresse = input("Quel est votre adresse ? ")

# Date d'aujourd'hui
today = datetime.datetime.now()

# Condition pour l'âge 
if today.year < annee:
    print("impossible")
else:
    age = today.year - annee

# Résultat 
print("Je soussigné", sexe, nom, prenom, 'né(e) le',date_de_naissance, "à",lieu_de_naissance, "demeurant", adresse, "certifie sur l'honneur l'exactitude des renseignements déclarés. Fait le", today.day, today.month, today.year)





