#!/usr/bin/env python

import re

class Display:
    SCREEN_WIDTH, SCREEN_HEIGHT = 50, 6
    screen = [[0] * SCREEN_WIDTH for _ in xrange (SCREEN_HEIGHT)]

    def rect(self, a, b):
        """ Turn on all pixels in the square axb starting from 0,0 """
        for i in xrange(b):
            for j in xrange(a):
                self.screen[i][j] = 1

    def rotateY(self, a, b):
        """ Shift column a by b times """
        tmp = []
        for i in xrange(self.SCREEN_HEIGHT):
            tmp.append(self.screen[i][a])
        tmp = tmp[self.SCREEN_HEIGHT-b:] + tmp[:self.SCREEN_HEIGHT-b]
        for i in xrange(self.SCREEN_HEIGHT):
            self.screen[i][a] = tmp[i]

    def rotateX(self, a, b):
        """ Shift row a by b times """
        self.screen[a] = self.screen[a][self.SCREEN_WIDTH-b:] + \
            self.screen[a][:self.SCREEN_WIDTH-b]

if __name__ == '__main__':
    d = Display()
    with open('d08.txt') as fp:
        for line in fp:
            print line
            m = re.match(r'rect (\d+)x(\d+)', line)
            if m:
                d.rect(int(m.group(1)), int(m.group(2)))
            m = re.match(r'rotate row y=(\d+) by (\d+)', line)
            if m:
                d.rotateX(int(m.group(1)), int(m.group(2)))
            m = re.match(r'rotate column x=(\d+) by (\d+)', line)
            if m:
                d.rotateY(int(m.group(1)), int(m.group(2)))

    # Part 1
    print sum([sum(x) for x in d.screen])

    # Part 2
    for x in d.screen:
        print ''.join(map(lambda y: str(y), map(lambda y: y or ' ', x)))