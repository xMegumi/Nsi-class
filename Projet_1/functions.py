import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def indices(lettre, mot):
    indice = []
    for i in range(len(mot)):
        if mot[i] == lettre:
            indice.append(i)
    return indice
