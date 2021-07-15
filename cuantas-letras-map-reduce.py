#!/usr/bin/env python

from functools import reduce


def cuantas_letras(frase):
    '''
    Args:
        frase: Una frase en una cadena, que no deberá contener signos de puntuación.
    Returns:
        el número de caracteres en las palabras de la frase.
    '''
    letras = reduce(lambda acc, n: acc + n,
                    map(lambda w: len(w), frase.split(" ")),
                    0)

    return f"La frase «{frase}» tiene {letras} letras"


print(cuantas_letras("En un lugar de La Mancha"))
print(cuantas_letras("Algo huele mal en Dinamarca"))
