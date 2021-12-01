#!/usr/bin/env python3

inp = []

with open('01.txt') as fp:
    for line in fp:
        inp.append(int(line.strip()))

def part1(inparr):
    count = 0
    lastval = inparr[0]
    for x in inparr[1:]:
        if x > lastval: count += 1
        lastval = x
    return count

def part2():
    narr = []
    for i in range(len(inp) - 2):
        narr.append(sum(inp[i:i+3]))
    return part1(narr)

print(part1(inp))
print(part2())
