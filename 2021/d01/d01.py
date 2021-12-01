#!/usr/bin/env python3

from typing import Counter


inp = []

with open('01.txt') as fp:
    for line in fp:
        inp.append(int(line.strip()))

def part1():
    count = 0
    lastval = inp[0]
    for x in inp[1:]:
        if x > lastval: count += 1
        lastval = x
    return count

def part2():
    return

print(part1())
print(part2())