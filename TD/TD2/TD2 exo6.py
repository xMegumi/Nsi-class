# -*- coding: utf-8 -*-
'''
:Titre : Opérateurs et expressions booléennes
:Auteur : Lorenzo
:Date : 1/10/2021

Exercice n°6 du TD n°2
'''

"""
Ecrire un programme qui détermine le nombre de mots dans le texte.
"""

texte = "Un ordinateur est un système de traitement de l'information programmable tel que défini par Alan Turing et qui fonctionne par la lecture séquentielle d'un ensemble d'instructions, organisées en programmes, qui lui font exécuter des opérations logiques et arithmétiques. Sa structure physique actuelle fait que toutes les opérations reposent sur la logique binaire et sur des nombres formés à partir de chiffres binaires. Dès sa mise sous tension, un ordinateur exécute, l'une après l'autre, des instructions qui lui font lire, manipuler, puis réécrire un ensemble de données déterminées par une mémoire morte d'amorçage. Des tests et des sauts conditionnels permettent de passer à l'instruction suivante et donc d'agir différemment en fonction des données ou des nécessités du moment ou de l'environnement. Le mot ordinateur fut introduit par IBM France en 19556,7 après que François Girard, alors responsable du service publicité de l'entreprise, eut l'idée de consulter son ancien professeur de lettres à Paris, Jacques Perret. Avec Christian de Waldner, alors président d'IBM France, ils demandèrent au professeur Perret, de suggérer un nom français pour sa nouvelle machine électronique destinée au traitement de l'information (IBM 650), en évitant d'utiliser la traduction littérale du mot anglais computer (calculateur ou calculatrice), qui était à cette époque plutôt réservé aux machines scientifiques.En 1911, une description de la machine analytique de Babbage utilisait le mot ordonnateur pour en décrire son organe moteur : Pour aller prendre et reporter les nombres… et pour les soumettre à l’opération demandée, il faut qu'il y ait dans la machine un organe spécial et variable : c'est l'ordonnateur. Cet ordonnateur est constitué simplement par des feuilles de carton ajourées, analogues à celle des métiers Jacquard… .Le professeur proposa un mot composé centré autour d'ordonnateur : celui qui met en ordre et qui avait aussi la notion d'ordre ecclésiastique dans l'église catholique (ordinant). Il suggéra plus précisément ordinatrice électronique, le féminin ayant pu permettre, selon lui, de mieux distinguer l'usage religieux de l'usage comptable du mot.IBM France retint le mot ordinateur et chercha au début à protéger ce nom comme une marque. Mais le mot fut facilement et rapidement adopté par les utilisateurs et IBM France décida au bout de quelques mois de le laisser dans le domaine public."

# Je créé une liste des mots 
liste_de_mots = texte.split()

# Puis je calcul le nombre de mots dans la liste
words_in_text = len(liste_de_mots)
print("Il y a", words_in_text,"mots dans le texte.")
