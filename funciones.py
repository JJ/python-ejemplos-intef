#!/usr/bin/env python

def al_cuadrado(dato):
    return dato*dato


def acumulador():
    if not "_contador" in dir(acumulador):
        acumulador._contador = 0
    acumulador._contador += 1
    return acumulador._contador


for _ in range(10):
    print(al_cuadrado(acumulador()))
