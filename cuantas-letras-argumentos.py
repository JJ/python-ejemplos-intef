#!/usr/bin/env python

palabras = "Se las lleva el viento"
print(palabras)


def cuantas_letras(frase, separador=r'\.|\s+'):
    '''
    Args:
        frase: Una frase en una cadena, que no deberá contener signos de puntuación.
        separador: Una expresión regular o cadena por la que se separarán las palabras.
    Returns:
        el número de caracteres en las palabras de la frase.
    '''
    palabras = frase.split(separador)
    letras = 0
    for p in palabras:
        letras += len(p)

    return f"La frase «{frase}» tiene {letras} letras con separador «{separador}»"


print(cuantas_letras("En un lugar de La Mancha", " "))
print(palabras)
print(cuantas_letras(frase="Algo huele mal en Dinamarca."))
