#!/usr/bin/env python

"""
1 2 3
4 5 6
7 8 9
"""

map = {
    'U': ([1, 2, 3], -3),
    'D': ([7, 8, 9],  3),
    'L': ([1, 4, 7], -1),
    'R': ([3, 6, 9],  1)
}

pos = 5

with open('d02.in') as fp:
    for line in fp:
        for c in line.strip():
            if pos not in map[c][0]:
                pos = pos + map[c][1]
        print pos