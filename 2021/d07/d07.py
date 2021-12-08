#!/usr/bin/env python3
import statistics

inp = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

with open('07.txt') as fp:
    inp = [int(x) for x in fp.read().strip().split(',')]


def part1(arr):
    median = statistics.median(arr)
    return sum([abs(x - median) for x in arr])


def part2(arr):
    narr = [0] * max(arr)
    for i in range(len(narr)):
        for w in arr:
            diff = abs(w - i)  # how many steps does the crab need to walk
            cost = diff * (diff + 1) / 2  # cost of the steps
            narr[i] += cost
    return min(narr)


print(part1(inp))
print(part2(inp))
