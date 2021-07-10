#!/usr/bin/env python

def fib():
    next = fib.first + fib.second
    (fib.first,fib.second) = (fib.second,next)
    yield next

fib.first = 1
fib.second = 1

for i in range(100):
    print(f"{i} → {next(fib())}")
