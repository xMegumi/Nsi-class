# -*- coding: utf-8 -*-
'''
:Titre : Découpage d'image
:Auteur : Lorenzo
:Date : 15/2021

Activité n°1 du TP n°3
'''

from PIL import Image                                               # utilisation d'une bibliothèque spécialisée pour l'image
"""
image_source = Image.open("pomme.jpg")                                  # ouverture du fichier "pomme.jpg"
# image_source.show()

largeur_image , hauteur_image = image_source.size                       # récupération des dimensions de l'image avec la fonction size()

image_quart1 = image_source.crop((0, 0, largeur_image//2, hauteur_image//2))        # création d'une nouvelle image par découpage rectangulaire de image_source 
              # coin supérieur gauche : 0,0      coin inférieur droit : largeur_image//2, hauteur_image//2

image_quart1.show()
image_quart1.save("quart1pomme.jpg")
"""

    
# Activité 1

image_source = Image.open("pomme.jpg") 
largeur_image , hauteur_image = image_source.size
image_quart1 = image_source.crop((0, 0, largeur_image//2, hauteur_image//2))
image_quart2 = image_source.crop((0, 250, 250, 500))
image_quart3 = image_source.crop((250, 250, 500, 500))
image_quart4 = image_source.crop((250, 0, 500, 250)) 

image_quart1.save("quart1pomme.jpg")
image_quart2.save("quart2pomme.jpg")
image_quart3.save("quart3pomme.jpg")
image_quart4.save("quart4pomme.jpg")
# image_quart2.show()
# image_quart3.show()
# image_quart4.show()

# Activité 2

image_rotate_1 = image_quart1.rotate(270)
image_rotate_1.save("image_rotate_1.jpg")
# image_rotate_1.show()

image_rotate_2 = image_quart2.rotate(90)
image_rotate_2.save("image_rotate_2.jpg")
# image_rotate_2.show()

image_rotate_3 = image_quart3.rotate(180)
image_rotate_3.save("image_rotate_3.jpg")
# image_rotate_3.show()

image_rotate_4 = image_quart4.rotate(90)
image_rotate_4.save("image_rotate_4.jpg")
# image_rotate_4.show()
pomme_decoupee = Image.open("pomme.jpg")

pomme_decoupee.paste(image_rotate_1,(0, 0, largeur_image//2, hauteur_image//2))
pomme_decoupee.paste(image_rotate_2,(250, 250, 500, 500))
pomme_decoupee.paste(image_rotate_3,(250, 0, 500, 250))
pomme_decoupee.paste(image_rotate_4,(0, 250, 250, 500))
pomme_decoupee.save("pomme_decoupee.jpg")
# pomme_decoupee.show()

# Activité 3

pomme = Image.open("pomme.jpg")
pomme_m = Image.open("pomme.jpg")
largeur_image , hauteur_image = image_source.size
new_size = (largeur_image//2, hauteur_image//2)
pomme_resize = pomme.resize(new_size)
pomme_resize.save("pomme_resize.jpg")
pomme_m.paste(pomme_resize)
pomme_m.paste(pomme_resize,(250,0))
pomme_m.paste(pomme_resize,(0,250))
pomme_m.paste(pomme_resize,(250,250))
pomme_m.save("pomme_m.jpg")
# pomme_m.show()

# Activité 4


def duplication(c):
    pomme = Image.open("pomme.jpg")
    largeur_image , hauteur_image = image_source.size
    source_size_largeur, source_size_hauteur = largeur_image // c, hauteur_image // c
    pomme_m = Image.new("RGB", (source_size_largeur * c,source_size_hauteur * c))
    pomme_m.show()
    pomme_m.save("pomme_m.jpg")
    new_size = (largeur_image//c, hauteur_image//c)
    pomme_resize = pomme.resize(new_size)
    pomme_resize.save("pomme_resize.jpg")
    for y in range(c):
        for x in range(c):
            pomme_m.paste(pomme_resize,(x*source_size_largeur,y*source_size_hauteur))
    pomme_m.save("pomme_m.jpg")
    pomme_m.show()
    
duplication(int(input("Entrez le nombre de pomme que vous voulez : ")))

    
