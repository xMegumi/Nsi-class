# -*- coding: utf-8 -*-
'''
:Titre : Opérateurs et expressions booléennes
:Auteur : Lorenzo
:Date : 30/09/2021

Exercice n°5 du TD n°2
'''

'''
Exercice 5 : Nombre de jours entre deux dates

Demander à l'utilisateur une première date (sous forme de nombres entiers) : • demander le jour et affecter sa réponse à la variable jour1. 
• demander le mois et affecter sa réponse à la variable mois1. • demander l'année et affecter sa réponse à la variable annee1.

Faites la même chose pour une deuxième date : jour2, mois2, annee2

Déterminer la date la plus ancienne des deux en déclarant les variables suivantes :
date1_jour, date1_mois, date1_annee : pour la date la plus ancienne
date2_jour, date2_mois, date2_annee : pour la date la plus récente

Déterminer le nombre de jours entre ces deux dates
'''

# Demande des dates à l'utilisateur


jour1, mois1, annee1 = int(input("Entrez le jour : ")), int(input("Entrez le mois : ")), int(input("Entrez l'année : "))
jour2, mois2, annee2 = int(input("Entrez le jour : ")), int(input("Entrez le mois : ")), int(input("Entrez l'année : "))

# Détermine la date la plus ancienne des deux : date1 = ancienne; date2 = recente 

if annee1 > annee2:
    date2_jour = jour1
    date2_mois = mois1
    date2_annee = annee1
    print(date2_jour, date2_mois, date2_annee, 'est la plus récente')
    date1_jour = jour2
    date1_mois = mois2
    date1_annee = annee2
    print(date1_jour, date1_mois, date1_annee, 'est la plus ancienne')
elif annee1 == annee2:
    if mois1 > mois2:
        date2_jour = jour1
        date2_mois = mois1
        date2_annee = annee1
        print(date2_jour, date2_mois, date2_annee, 'est la plus récente')
        date1_jour = jour2
        date1_mois = mois2
        date1_annee = annee2
        print(date1_jour, date1_mois, date1_annee, 'est la plus ancienne')
    elif mois1 == mois2:
        if jour1 > jour2:
            date2_jour = jour1
            date2_mois = mois1
            date2_annee = annee1
            print(date2_jour, date2_mois, date2_annee, 'est la plus récente')
            date1_jour = jour2
            date1_mois = mois2
            date1_annee = annee2
            print(date1_jour, date1_mois, date1_annee, 'est la plus ancienne')
        elif jour1 == jour2:
            print("Vous avez inscrit les mêmes dates.")
            print("Le nombre de jour entre les deux dates est donc de : 0")
            exit()
        else:
            date2_jour = jour2
            date2_mois = mois2
            date2_annee = annee2
            print(date2_jour, date2_mois, date2_annee, "est la plus récente")
            date1_jour = jour1
            date1_mois = mois1
            date1_annee = annee1
            print(date1_jour, date1_mois, date1_annee, 'est la plus ancienne')
    else:
        date2_jour = jour2
        date2_mois = mois2
        date2_annee = annee2
        print(date2_jour, date2_mois, date2_annee, "est la plus récente")
        date1_jour = jour1
        date1_mois = mois1
        date1_annee = annee1
        print(date1_jour, date1_mois, date1_annee, 'est la plus ancienne')
else:
    date2_jour = jour2
    date2_mois = mois2
    date2_annee = annee2
    print(date2_jour, date2_mois, date2_annee, "est la plus récente")
    date1_jour = jour1
    date1_mois = mois1
    date1_annee = annee1
    print(date1_jour, date1_mois, date1_annee, 'est la plus ancienne')


""" Determine le nombre de jours entre les dates """
est_bissextile = False
nb_jours_total = 0
first_year = False
last_year = False
nb_jours_debut = 0

# Variable utile pour calculer le nombre de jours restant d'une année utile pour le calcul de la première année 
nb_jours_temporaire = 0

# Dictionnaire avec tout les mois
month_dictionary = {"janvier" : 31, "fevrier" : 28, "mars": 31, "avril": 30, "mai": 31, "juin": 30, "juillet": 31, "aout": 31, "septembre": 30, "octobre": 31, "novembre": 30, "decembre": 31}

# Calcul le nombre de jours de la première année + addition des jours au total
date1_mois -= 1
nb_jours_total += date1_jour -1

# Vérifie si l'année de la plus ancienne date est bissexitle ou non + ajoute en conséquence le mounth_dictionary
if(date1_annee%4==0 and date1_annee%100!= 0 or date1_annee%400==0):
    month_dictionary.update({"fevrier": 29})
    est_bissextile = True
else:
    est_bissextile = False
    month_dictionary.update({"fevrier": 28})

# Calcul le nombre de jours du début de l'année jusqu'à la date
first_year = True
if date1_annee != date2_annee:
    for key,value in month_dictionary.items():
        for i in range(date1_annee, date2_annee):
            if date1_mois > 0:
                nb_jours_temporaire += value
                date1_mois -= 1
            else:
                continue
else:    
    for key, value in month_dictionary.items():
        if date2_mois <= date1_mois:
            nb_jours_debut += value
            date2_mois -= 1
        else:
            break
    nb_jours_debut -= date1_jour
    date2_jour = date2_jour - 1
    nb_jours_total += nb_jours_debut + date2_jour
        
   
# Calcul grâce au nombre de jours du début de la plus ancienne année le nombre de jours restant + les additions au total
if est_bissextile == True and date1_annee != date2_annee:
    annee_f = 366
    nb_jours_total += annee_f - nb_jours_temporaire
elif est_bissextile == False and date1_annee != date2_annee:
    annee_f = 365
    nb_jours_total += annee_f - nb_jours_temporaire

# Calcul le nombre de jours de la dernière année si ce n'est pas la même que la première + addition des jours au total
if date1_annee != date2_annee:
    nb_jours_total += date2_jour -1
    if date1_mois != date2_mois:
        date2_mois -= 1

# Vérifie si l'année de la plus récente date est bissextile ou non + ajoute en conséquence le mounth_dictionary
if(date2_annee%4==0 and date2_annee%100!= 0 or date2_annee%400==0):
    month_dictionary.update({"fevrier": 29})
    est_bissextile = True
else:
    est_bissextile = False
    month_dictionary.update({"fevrier": 28})

# Calcul le nombre de jours du début de l'année jusqu'à la date
if date1_annee != date2_annee:
    for key, value in month_dictionary.items():
        last_year = True
        if date2_mois > 0:
            nb_jours_total += value
            date2_mois -= 1
        else:
            continue

# Calcul du nombre de jours des années/mois/jours restant + additions des jours au total
if first_year == True and last_year == True:
    tour = 2
elif first_year == True and last_year == False:
    tour = 1

if date2_annee - date1_annee > 0:
    for i in range(date1_annee + 1, date2_annee):
        if(i%4==0 and i%100!= 0 or i%400==0):
            month_dictionary.update({"fevrier": 29})
            est_bissextile = True
        else:
            month_dictionary.update({"fevrier": 28})

        for key,value in month_dictionary.items():
            nb_jours_total += value
    print("Le nombre de jours entre les deux dates est de :", nb_jours_total, "jours")
else:
    print("Le nombre de jours entre les deux dates est de :", nb_jours_total, "jours")
