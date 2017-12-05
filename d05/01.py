#!/usr/bin/env python3

# Part 1
input = [0, 3, 0, 1, -3]
with open('input.txt', 'r') as fp:
    input = [int(x) for x in fp.read().split()]

steps = 0
pos = 0
while True:
    newpos = pos + input[pos]
    input[pos] += 1
    pos = newpos
    steps += 1
    if pos >= len(input) or pos < 0: break

print(steps)

# Part 2
input = [0, 3, 0, 1, -3]
with open('input.txt', 'r') as fp:
    input = [int(x) for x in fp.read().split()]

steps = 0
pos = 0
while True:
    newpos = pos + input[pos]
    if newpos - pos >= 3:
         input[pos] -= 1
    else:
        input[pos] += 1
    steps += 1
    pos = newpos
    if pos >= len(input) or pos < 0: break

print(steps)