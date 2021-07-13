#!/usr/bin/env python

al_cuadrado = lambda dato: dato*dato


def acumulador():
    if not "_contador" in dir(acumulador):
        acumulador._contador = 0
    acumulador._contador += 1
    return acumulador._contador


for _ in range(10):
    print(al_cuadrado(acumulador()))
