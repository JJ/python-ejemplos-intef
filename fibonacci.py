#!/usr/bin/env python

def fib(n):
    if n <= 2:
        return 1
    if n <= 3:
        return 2
    return fib(n-1)+fib(n-2)


for i in range(33):
    print(f"{i} → {fib(i)}")
