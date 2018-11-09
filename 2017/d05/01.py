#!/usr/bin/env python3

def calc(input, part2):
    steps = 0
    pos = 0
    while True:
        newpos = pos + input[pos]
        if part2 and (newpos - pos >= 3):
            input[pos] -= 1
        else:
            input[pos] += 1
        pos = newpos
        steps += 1
        if pos >= len(input) or pos < 0: break
    return steps


# Example
print(calc([0, 3, 0, 1, -3], True))
print(calc([0, 3, 0, 1, -3], False))

input = []

# Part 1
with open('input.txt', 'r') as fp: input = [int(x) for x in fp.read().split()]
print(calc(input, False))
# Part 2
with open('input.txt', 'r') as fp: input = [int(x) for x in fp.read().split()]
print(calc(input, True))