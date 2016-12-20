#!/usr/bin/env python

class Blacklist:

    counter = 0
    ranges = []
    def __init__(self):
        with open('d20.txt') as fp:
            for line in fp:
                self.ranges.append([int(x) for x in line.rstrip().split('-')])
        self.ranges.sort()

    def locate(self):
        for start, end in self.ranges:
            if self.counter >= start and self.counter <= end:
                self.counter = end + 1
        return self.counter

    
    def squash(self, p1, p2):
        """ Squashes overlapping arrays. Three possibilities,
        1. (a1, b1)
                        (a2, b2)
            Do nothing
        2. (a1,        b1)
              (a2, b2)
            Return (a1, b1)
        3. (a1,         b1)
                    (a2,        b2)
            Return (a1, b2)
        """
        (a1, b1), (a2, b2) = p1, p2
        if a2 > b1:
            return [(a1, b1), (a2, b2)]
        elif a2 >= a1 and b2 <= b1:
            return[(a1, b1)]
        elif a2 >= a1 and a2 <= b1 and b2 > b1:
            return [(a1, b2)]
        else:
            throw

    def count(self):
        tmp = []
        for i in xrange(0, len(self.ranges)-1, 2):
            tmp.extend(self.squash(self.ranges[i], self.ranges[i+1]))
        return tmp
    

if __name__ == '__main__':
    b = Blacklist()
    print b.locate()
    oldcount = len(b.ranges)
    while True:
        b.ranges = b.count()
        if len(b.ranges) == oldcount:
            break
        print oldcount, len(b.ranges)
        oldcount = len(b.ranges)