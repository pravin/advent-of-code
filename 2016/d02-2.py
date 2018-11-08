#!/usr/bin/env python

"""
    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""

"""
ULL     5
RRDDD   D
LURDL   B
UUUUD   3
"""

pad = [
    [None, None, '1', None, None],
    [None, '2',  '3', '4',  None],
    ['5',  '6',  '7', '8',  '9'],
    [None, 'A',  'B', 'C',  None],
    [None, None, 'D', None, None]
]

map = {
    'U': (-1,  0),
    'D': ( 1,  0),
    'L': ( 0, -1),
    'R': ( 0,  1)
}

pos = (2, 0)

with open('d02.in') as fp:
    for line in fp:
        for c in line.strip():
            move = map[c]
            pos2 = pos[0] + move[0], pos[1] + move[1]
            if pos2[0] in range(5) and pos2[1] in range(5): # Not out of bounds
                if pad[pos2[0]][pos2[1]] != None: 
                    pos = pos2
        print pad[pos[0]][pos[1]]