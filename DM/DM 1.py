# -*- coding: utf-8 -*-
'''
:Titre : DM 1
:Auteur : Lorenzo
:Date : 08/12/2021

DM n°1
'''

'''
Écrire un programme qui demande à l'utilisateur le nom d'un verbe du premier groupe et qui affiche sa
conjugaison au présent de l'indicatif
'''

import random


def last_letter(word, number):
    '''Documentation:
La fonction retourne le(s) 'number' dernière(s) lettre(s) du mot 'word'.
:param: mot and number, type str and type int
:return: str

Example:
>>> last_letter("prier", 2):
'er'
>>> last_letter("fatiguer", 4):
'guer'
    '''
    word = list(word)
    output = []
    for i in range(1, number + 1):
        output.append(word[-i])
    output.reverse()
    return "".join(output)

def termination(mot):
    '''Documentation:
la fonction retour le mot en changeant les terminaisons au présent de
l'indicatif.
:param: mot, type list
:return: list
:CU: L'argument doit être une liste des lettres d'un verbe du premier groupe.
    
Example:
>>> termination('prier')
['prie', 'pries', 'prie', 'prions', 'priez', 'prient']
>>> termination('parler')
['parle', 'parles', 'parle', 'parlons', 'parlez', 'parlent']
'''
    dico_term = {1 : 'e', 2: 'es', 3: 'e', 4: 'ons', 5: 'ez', 6: 'ent'}
    output = []
    del mot[-1]
    del mot[-1]

    for i in range(1, 7):
        output.append(''.join(mot) + dico_term[i])

    return output

<<<<<<< HEAD
start_end = ''
choix = ''
# Boucle du programme
while start_end != 'stop':
# Création du choix manuel ou random (facultatif).
    random_v = random.choice((open('DM/first_group_verb.txt', 'r')).readlines())
    if choix != 'manuel' and choix != 'random':

        while choix != 'manuel' and choix != 'random':
            choix = input("Souhaitez-vous choisir le verbe ou générer automatiquement un verbe ?. [manuel/random] \n").lower()
            if choix == 'random':
                verb = random_v
                print("Le verbe choisi est :", verb)
                verb = list(verb)
                verb.remove('\n')
            elif choix == 'manuel':
                verb = str(input("Veulliez entrer un verbe : "))
                while last_letter(verb, 2) != 'er':
                    print("Vous n'avez pas entrer un verbe du premier groupe.")
                    verb = str(input("Veulliez entrer un verbe : "))
                verb = list(verb)
            else:
                print("Entrer un choix correcte : [manuel ou random]")
    else:
        if choix == 'random':
                verb = random_v
                print("Le verbe choisi est :", verb)
                verb = list(verb)
                verb.remove('\n')
        elif choix == 'manuel':
            verb = str(input("Veulliez entrer un verbe : "))
            while last_letter(verb, 2) != 'er':
                print("Vous n'avez pas entrer un verbe du premier groupe.")
                verb = str(input("Veulliez entrer un verbe : "))
            verb = list(verb)


    # Sert pour les dernières exceptions des conditions.
    verb_e_5l = ['ébrer', 'écher', 'écrer', 'égler', 'égner', 'égrer', 'éguer', 'équer', 'étrer', 'évrer',]
    verb_e_4l = ['écer', 'éder', 'éler', 'émer', 'éner', 'érer', 'éser', 'éter', 'éyer']

    # Sert à l'affichage
    pronon = ("Je/J'", "Tu/T'", "Il/Elle", 'Nous', 'Vous', 'Ils/Elles')


    # Première condition pour les verbes 'cer' qui prennent une cédille pour 'nous'
    if last_letter(verb, 3) == 'cer':
        conj = termination(verb)
        nous = str(conj[3]).replace('c','ç')
        conj[3] = nous

        output = conj

    # Deuxième condition pour les verbes en "ger" qui gardent le "e" pour 'nous'.
    elif last_letter(verb, 3) == 'ger':
        conj = termination(verb)
        nous_last_letter = last_letter(str(conj[3]), 3)
        nous = str(conj[3]).replace(nous_last_letter, "eons")
        conj[3] = nous
        output = conj

    # Troisième condition pour les verbes qui se termient en 'ayer', 'uyer', 'oyer' où le 'y' devient un 'i'.
    elif last_letter(verb, 4) == 'ayer' or last_letter(verb, 4) == 'uyer' or last_letter(verb, 4) == 'oyer':
        verb[-3] = 'i'
        output = termination(verb)

    # Quatrième condition pour les verbes en 'eler' qui double leur 'l'
    elif last_letter(verb, 4) == 'eler':
        verb[-2] = 'l'
        verb[-1] = 'e'
        verb.append('r')
        conj = termination(verb)

        nous = str(conj[3]).replace('l','')
        vous = str(conj[4]).replace('l','')
        conj[3] = nous
        conj[4] = vous

        output = conj

    # Cinquième condition pour les verbes en 'eter' qui double leur 't'.
    elif last_letter(verb, 4) == 'eter':
        verb[-2] = 't'
        verb[-1] = 'e'
        verb.append('r')
        conj = termination(verb)

        nous = str(conj[3]).replace('t','')
        vous = str(conj[4]).replace('t','')
        conj[3] = nous
        conj[4] = vous

        output = conj

    # sixième condition pour toutes les terminaisons dans la liste 'verb_e_4l' qui prennet un 'é' sauf pour 'nous' et 'vous'.
    elif last_letter(verb, 4) in verb_e_4l:
        verb[-4] = 'è'
        conj = termination(verb)

        nous = str(conj[3]).replace('è','é')
        vous = str(conj[4]).replace('è','é')
        conj[3] = nous
        conj[4] = vous

        output = conj

    # septième condition pour toutes les terminaisons dans la liste 'verb_e_5l' qui prennet un 'é' sauf pour 'nous' et 'vous'.
    elif last_letter(verb, 5) in verb_e_5l:
        verb[-5] = 'è'
        conj = termination(verb)

        nous = str(conj[3]).replace('è','é')
        vous = str(conj[4]).replace('è','é')
        conj[3] = nous
        conj[4] = vous

        output = conj

    # Dernière condition qui remplacer juste 'er' par les bonnes terminaisons.
    else:
        output = termination(verb)

    place = 0

    for conjugais in output:
        print(pronon[place], conjugais)
        place += 1
    start_end = input("Souhaitez-vous continuer ou arrêter le programme ? [stop/*] \n")
=======

verb = str(input("Veulliez entrer un verbe : "))
verb_e_5l = ['ébrer', 'écher', 'écrer', 'égler', 'égner', 'égrer', 'éguer', 'équer', 'étrer', 'évrer',]
verb_e_4l = ['écer', 'éder', 'éler', 'émer', 'éner', 'érer', 'éser', 'éter', 'éyer']
verb = list(verb)


if last_letter(verb, 3) == 'cer':
    conj = termination(verb)
    nous = str(conj[3]).replace('c','ç')
    conj[3] = nous

    output = conj

elif last_letter(verb, 3) == 'ger':
    conj = termination(verb)
    nous = str(conj[3]).replace('c','ç')
    conj[3] = nous
    output = conj

elif last_letter(verb, 4) == 'ayer' or last_letter(verb, 4) == 'uyer' or last_letter(verb, 4) == 'oyer':
    verb[-3] = 'i'
    output = termination(verb)

elif last_letter(verb, 4) == 'eler':
    verb[-2] = 'l'
    verb[-1] = 'e'
    verb.append('r')
    conj = termination(verb)

    nous = str(conj[3]).replace('l','')
    vous = str(conj[4]).replace('l','')
    conj[3] = nous
    conj[4] = vous

    output = conj

elif last_letter(verb, 4) == 'eter':
    verb[-2] = 't'
    verb[-1] = 'e'
    verb.append('r')
    conj = termination(verb)

    nous = str(conj[3]).replace('t','')
    vous = str(conj[4]).replace('t','')
    conj[3] = nous
    conj[4] = vous

    output = conj

elif last_letter(verb, 4) in verb_e_4l:
    verb[-4] = 'è'
    conj = termination(verb)

    nous = str(conj[3]).replace('è','é')
    vous = str(conj[4]).replace('è','é')
    conj[3] = nous
    conj[4] = vous

    output = conj

elif last_letter(verb, 5) in verb_e_5l:
    verb[-5] = 'è'
    conj = termination(verb)

    nous = str(conj[3]).replace('è','é')
    vous = str(conj[4]).replace('è','é')
    conj[3] = nous
    conj[4] = vous

    output = conj


print(output)
>>>>>>> fee5d78076a69ecebb03fec3403b0928a856cc5f
