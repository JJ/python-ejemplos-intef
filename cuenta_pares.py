from functools import reduce
from random import random
aleatorios = [int(random()*10000) for _ in range(10000)]


def cuenta_pares(prev, this):
    prev[this & 1] += 1
    return prev


print(reduce(cuenta_pares, aleatorios, [0, 0]))
