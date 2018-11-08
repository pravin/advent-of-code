#!/usr/bin/env python
import re

count = 0

with open('d03.in') as fp:
    for line in fp:
        sides = [int(x) for x in re.split('\s+', line.strip())]
        sides.sort()
        if sides[0] + sides[1] > sides[2]: count +=1

print count