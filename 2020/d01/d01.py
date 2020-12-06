#!/usr/bin/env python3

inp = []

with open('input.txt') as fp:
    for line in fp:
        inp.append(int(line.strip()))

inp.sort()

# Part 1
def part1(the_sum, endpos):
    for i in range(endpos-1):
        if inp[i] > the_sum: break
        for j in range(endpos-1, i, -1):
            if inp[j] > the_sum: continue
            if inp[i] + inp[j] == the_sum:
                return (i, j)
    return None, None

i, j = part1(2020, len(inp))
print("Part 1:", inp[i] * inp[j])


# Part 2
def part2():
    for k in range(len(inp)-1, 2, -1): # At minimum, we need 2 other elements
        if inp[k] > 2020: continue
        i, j = part1(2020 - inp[k], k)
        if i == None: continue
        if inp[k] + inp[i] + inp[j] == 2020:
            return inp[k] * inp[i] * inp[j]

print ("Part 2:", part2())
