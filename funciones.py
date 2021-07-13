#!/usr/bin/env python

def al_cuadrado(dato):
    return dato*dato


def acumulador():
    acumulador._contador += 1
    return acumulador._contador


acumulador._contador = 0

for _ in range(10):
    print(al_cuadrado(acumulador()))
