#!/usr/bin/env python

def cuantas_letras(frase):
    palabras = frase.split(" ")
    letras = 0
    for p in palabras:
        letras += len(p)

    return f"La frase «{frase}» tiene {letras} letras"


print(cuantas_letras("En un lugar de La Mancha"))
print(cuantas_letras("Algo huele mal en Dinamarca"))
