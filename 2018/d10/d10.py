#!/usr/bin/env python
import re

class Day10:
    _input = []
    SIZE = 100
    def __init__(self):
        with open('input.txt') as fp:
            for line in fp:
                # id, x, y, width, height
                matchObj = re.match(r"position=<(.*?),(.*?)> velocity=<(.*?),(.*?)>", line)
                self._input.append((
                    int(matchObj.group(1)), 
                    int(matchObj.group(2)), 
                    int(matchObj.group(3)),
                    int(matchObj.group(4))
                ))

    def puzzle1(self):
        count = 0
        while True:
            x_coords = [x[0] for x in self._input]
            y_coords = [x[1] for x in self._input]
            min_x = min(x_coords)
            min_y = min(y_coords)
            width = max(x_coords) - min_x
            height = max(y_coords) - min_y
            if width <= self.SIZE and height <= self.SIZE:
                self.print_sky(width, height, min_x, min_y)
                if input() != '': break
            # Move points
            for i in range(len(self._input)):
                x, y, vx, vy = self._input[i]
                self._input[i] = x + vx, y + vy, vx, vy
            count += 1
        return count


    def print_sky(self, width, height, min_x, min_y):
        fabric = [['.'] * (width+1) for x in range(height+1)]
        for x, y, vx, vy in self._input:
            fabric[y-min_y][x-min_x] = '#'
        for x in fabric:
            print(''.join(x))


if __name__ == '__main__':
    d = Day10()
    print(d.puzzle1())