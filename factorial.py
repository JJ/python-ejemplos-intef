#!/usr/bin/env python

import functools


@functools.lru_cache(maxsize=1024)
def factorial(n):
    if n <= 2:
        return n
    return n*factorial(n-1)


for i in range(1000):
    print(f"{i} → {factorial(i)}")
