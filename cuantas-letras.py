#!/usr/bin/env python

def cuantas_letras(frase):
    '''
    Args:
        frase: Una frase en una cadena, que no deberá contener signos de puntuación.
    Returns:
        el número de caracteres en las palabras de la frase.
    '''
    palabras = frase.split(" ")
    letras = 0
    for p in palabras:
        letras += len(p)

    return f"La frase «{frase}» tiene {letras} letras"


print(cuantas_letras("En un lugar de La Mancha"))
print(cuantas_letras("Algo huele mal en Dinamarca"))
