#!/usr/bin/env python

import re

count = 0

arr = [[], [], []]

with open('d03.in') as fp:
    for line in fp:
        sides = [int(x) for x in re.split('\s+', line.strip())]
        for i in range(3):
            arr[i].append(sides[i])

sides = arr[0] + arr[1] + arr[2]
for i in xrange(0, len(sides), 3):
    tri = [sides[i], sides[i+1], sides[i+2]]
    tri.sort()
    if tri[0] + tri[1] > tri[2]: count +=1

print count