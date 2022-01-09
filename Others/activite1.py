from PIL import Image # utilisation d'une bibliothèque spécialisée pour l'image

# Activité 1
"""
img = Image.open("pomme.jpg")           # ouverture du fichier

r,v,b=img.getpixel((250,300))           # code R V B du pixel de coordonnées (100,250)

print("canal rouge : ",r,"    canal vert : ",v,"    canal bleu : ",b)     # affichage du code R V B

image.putpixel((250,250),(255,0,0))
"""

# Activité 2
"""
image = Image.open("pomme.jpg")
image.putpixel((250,250),(255,0,0))

image.show()
image.save("pomme2.jpg")

# b) On peut apercevoir un pixel rouge
"""

# Activité 3
"""
image = Image.open("pomme.jpg")
largeur_image = 500
hauteur_image = 500

for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b = image.getpixel((x,y))
        new_r = v
        new_v = b
        new_b = r
        image.putpixel((x,y),(new_r,new_v,new_b))

image.show()
image.save("pomme3.jpg")
# Le programme va aller à chaque cordonnée pour modifier la couleur de la pomme, cela donne un resultat violet.
"""

# Activité 4
"""
image = Image.open("pomme.jpg")
largeur_image = 500
hauteur_image = 500

for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b = image.getpixel((x,y))
        new_r = b
        new_v = v
        new_b = r
        image.putpixel((x,y),(new_r,new_v,new_b))

image.show()
image.save("pomme4.jpg")
"""

# Activité 5
"""
image = Image.open("pomme.jpg")
largeur_image = 500
hauteur_image = 500

for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b = image.getpixel((x,y))
        new_r = 255-r
        new_v = 255-v
        new_b = 255-b
        image.putpixel((x,y),(new_r,new_v,new_b))

image.show()
image.save("pomme5.jpg")
"""

# Activité 6
"""
image = Image.open("pomme.jpg")
largeur_image = 500
hauteur_image = 500

for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b = image.getpixel((x,y))
        gray = 0.2989*r + 0.5870*v + 0.1140*b
        new_r = int(gray)
        new_v = int(gray)
        new_b = int(gray)
        image.putpixel((x,y),(new_r,new_v,new_b))

image.show()
image.save("pomme8.jpg")
"""

# Activité 7
"""
image = Image.open("pomme.jpg")
largeur_image = 500
hauteur_image = 500

for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b = image.getpixel((x,y))
        new_r = r
        new_v = v
        if b < 200 :
            new_b = 255-b
        else :
            new_b = b
        image.putpixel((x,y),(new_r,new_v,new_b))

image.show()
image.save("pomme7.jpg")
# Le programme transforme le pixel bleu en négatif si il est inferieur
# à 200 sinon il laisse les couleurs originales
"""