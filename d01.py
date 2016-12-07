#!/usr/bin/env python

import re

fp = open('d01.in')
inp = fp.read()
fp.close()

pos = (0, 0)
orientation = (1, 0) # Starting state: Pointing North

ochange = {
            (-1, 0): (0, -1),
            (1, 0):  (0, 1), 
            (0, 1): (-1, 0),
            (0, -1): (1, 0), 
        }

for s in re.split(',\s', inp):
    idx = int(s[1:])
    orientation = ochange[orientation]
    if s[0] == 'L': orientation = orientation[0] * -1, orientation[1] * -1
    pos = idx * orientation[0] + pos[0], idx * orientation[1] + pos[1]
    #print '>', s, pos, orientation

print sum([abs(p) for p in pos])
