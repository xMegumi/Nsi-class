# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 14/11/2021

Exercice n°6 du TD n°3
'''

'''
a) Établir un tableau ordonnée des pièces et billets en euros.
b) Établir une fonction rendu qui prend en paramètre un prix et un paiement, qui retourne le rendu monnaie sous forme d'un tableau
'''

euros = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
# Création d'un dictionnaire contenant le futur nombre de billet/pièce à rendre
monnaie = {}

def rendu_monnaie(prix, paiement):
    # Condition pour savoir si l'acheteur a l'argent pour l'acheté ou si il paye la somme exactement
    if prix >= paiement:
        return 0

    # Calcul la somme à rendre, le prix x100 converti le prix en centime
    rendre = paiement * 100 - prix * 100

    #Création de la boucle principale
    for i in euros:
        # Condition pour savoir si le montant à rendre divisé par la liste d'argent est supérieur à 0
        if rendre // i > 0:
            # Ajoute le nombre de billet/pièces à rendre
            monnaie[i//100] = rendre // i
            # Calcule le rendu
            rendre = rendre % i

    return rendre

rendu_monnaie(200,220)
print(monnaie)
