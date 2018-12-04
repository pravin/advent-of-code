#!/usr/bin/env python3

import re

class Day03:
    _input = []
    FABRIC_SIZE = 1000
    
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
        fabric = [[0] * self.FABRIC_SIZE for x in range(self.FABRIC_SIZE)]
        for id, x, y, w, h in self._input:
            # Increment (x, y) locations in fabric
            for i in range(w):
                for j in range(h):
                    fabric[y+j][x+i] += 1
        count = 0
        for i in range(self.FABRIC_SIZE):
            for j in range(self.FABRIC_SIZE):
                if fabric[i][j] > 1:
                    count += 1

        return count

    
    def puzzle2(self):
        ids = set()
        for i in range(len(self._input) - 1):
            for j in range(i+1, len(self._input)):
                id1, x1, y1, w1, h1 = self._input[i]
                id2, x2, y2, w2, h2 = self._input[j]

                # Check if the rectagles overlap
                # Logic from https://www.geeksforgeeks.org/find-two-rectangles-overlap/
                if x1 >= x2+w2 or x2 >= x1+w1: 
                    continue
                if y1 >= y2+h2 or y2 >= y1+h1:
                    continue
                ids = ids.union({id1, id2})

        return set(range(1, len(self._input)+1)).difference(ids)


if __name__ == '__main__':
    d = Day03()
    print(d.puzzle1())
    print(d.puzzle2())
