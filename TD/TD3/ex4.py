# -*- coding: utf-8 -*-
'''
:Titre : liste et tableau
:Auteur : Lorenzo
:Date : 08/11/2021

Exercice n°4 du TD n°3
'''

'''
1) Créez 4 tableaux hiver, printemps, ete et automne contenant les mois correspondants à ces saisons.
2) Créez ensuite un tableau saisons contenant les tableaux hiver, printemps, ete et automne.
3) Prévoyez ce que renvoient les instructions suivantes, puis vérifiez-le dans l'interpréteur :
    a) saisons[2] 
b) saisons[1][0] 
c) saisons[1:2] 
d) saisons[:][1].
Comment expliquez-vous ce dernier résultat ?
'''

hiver = ['decembre', 'janvier', 'fevrier']
printemps = ["mars","avril","mai"]
ete = ["juin", "juillet", "aout"]
automne = ["septembre", "octobre", "novembre"]

saisons = [hiver,  printemps,  ete,  automne]

# Nous pouvons expliquer ce dernier résultat (saisons[:][1]), la première instruction "[:]" précise aucun tableau spécifique python 
# va alors prendre les tableaux du début jusqu'à la fin ce qui va constituer un seul tableau avec toutes les saisons ensuite dans ce tableau nous demandons 
# l'élement "[1]", 0 étant l'hiver le printemps le 1 il va donc afficher les mois de printemps.
print(saisons[:][1])
