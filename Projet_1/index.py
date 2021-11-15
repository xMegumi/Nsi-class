import random 

from functions import remove_accents, indices

# Génère un mot aléatoire à partir du fichier txt "liste_francais"
random_words = random.choice(open("Projet_1\list_of_french_words.txt","r").readlines())
words = random_words.upper()
words = list(remove_accents(words))
words.remove("\n")


# Création des variables utiles au programme.
affichage = []
erreur = 0
lettre_memoire = []

# Fabrication de l'affichage les caractères deviennent des "*" et les espaces deviennent des "-".
for i in range(len(words)):
    if words[i] == " ":
        words[i] = "-"
        affichage.append("-")
    else:
        affichage.append("*")

# Boucle principale du programme.
print(*affichage)
while erreur < 8:
    if affichage == words:
        print('Bravo, vous avez gagné !')
        quit()
    else:
        lettre = str(input("Entrez une lettre : ")).upper()
        if len(lettre) != 1:
            print("Entrer une seule lettre.")
        else:
            if lettre in lettre_memoire:
                print("Cette lettre à déjà été utilisé.")
            elif lettre in words:
                lettre_memoire.append(lettre)
                for i in indices(lettre, words):
                    affichage[i] = lettre
                print(*affichage)
            else:
                erreur += 1
                print("Vous avez fait ", erreur, "erreurs.")
                print(*affichage)
                
print("Vous avez perdu. Le mot était", *words)
