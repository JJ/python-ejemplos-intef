#!/usr/bin/env python

import random

uno_al_tres = random.randint(1,3)
color = random.choice(['rojo','verde','azul'])

print( f'Se ha generado {color} y {uno_al_tres}')
