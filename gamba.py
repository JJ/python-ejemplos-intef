#!/usr/bin/env python

from itertools import accumulate

gamba = "gamba"[:]

print(list(accumulate(gamba, lambda l1, l2: l1 + l2 )))
