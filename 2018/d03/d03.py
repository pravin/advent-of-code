#!/usr/bin/env python3

import re

class Day03:
    _input = []
    
    def __init__(self):
        with open('input.txt') as fp:
            for line in fp:
                # id, x, y, width, height
                matchObj = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
                self._input.append((
                    int(matchObj.group(1)), 
                    int(matchObj.group(2)), 
                    int(matchObj.group(3)),
                    int(matchObj.group(4)),
                    int(matchObj.group(5))
                ))

    def puzzle1(self):
        fabric = [[0] * 1000 for x in range(1000)]
        for id, x, y, w, h in self._input:
            # Increment (x, y) locations in fabric
            for i in range(w):
                for j in range(h):
                    fabric[x+i][y+j] += 1
        count = 0
        for i in range(len(fabric)):
            for j in range(len(fabric)):
                if fabric[i][j] > 1:
                    count += 1
        return count
        

if __name__ == '__main__':
    d = Day03()
    print(d.puzzle1())
