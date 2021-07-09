git st#!/usr/bin/env python

import random

uno_al_tres = random.randint(1,3)
while uno_al_tres != 3:
    uno_al_tres = random.randint(1,3)
    print(f"Otra vez será, salió {uno_al_tres}")

print("A la tercera fue la vencida")
