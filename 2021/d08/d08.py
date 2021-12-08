#!/usr/bin/env python3

inp = []
with open('08.txt') as fp:
    for line in fp:
        signal_patterns, output_value = line.strip().split('|')
        p1 = signal_patterns.strip().split(' ')
        p2 = output_value.strip().split(' ')
        inp.append((p1, p2))

def part1(arr):
    count = 0
    for p1, p2 in arr:
        for x in p2:
            if len(x) in [2, 3, 4, 7]:
                count += 1
    return count

print(part1(inp))