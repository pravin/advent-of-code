#!/usr/bin/env python

"""
Algorithm

Use a hashmap to store visited locations
Exit on hit to hashmap

"""

import re

visited = {(0,0): 1}

def getInputArray():
    """ Plumbing: Get input """
    with open('d01.in') as fp:
        return re.split(',\s', fp.read())

def moveTo(pos, inc):
    """ 
    Marks all steps from initial to final point as visited
    Returns new x, y location
    """
    for i in range(2):
        step = 1
        if inc[i] == 0: continue
        if inc[i] < 0: step = -1
        for pos[i] in xrange(pos[i]+step, pos[i] + inc[i] + step, step):
            if visited.has_key((pos[0], pos[1])):
                return pos, abs(pos[0]) + abs(pos[1])
            visited[(pos[0], pos[1])] = 1
    return pos, -1
    
    

def walk(ar):
    pos = [0, 0]
    orientation = (1, 0) # Starting state: Pointing North

    ochange = {
                (-1, 0): (0, -1),
                (1, 0):  (0, 1), 
                (0, 1): (-1, 0),
                (0, -1): (1, 0), 
            }

    res = -1
    for s in ar:
        idx = int(s[1:])
        orientation = ochange[orientation]
        if s[0] == 'L': orientation = orientation[0] * -1, orientation[1] * -1
        
        pos, res = moveTo(pos, [x * idx for x in orientation])
        if res != -1: break
    return res


if __name__ == '__main__':
    ar = getInputArray()
    print walk(ar)
