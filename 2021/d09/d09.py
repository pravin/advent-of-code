#!/usr/bin/env python3

# 1: Use test input
# 0: Use final input
DEBUG = 0
filename = ["09.txt", "09-test.txt"]

inp = []
with open(filename[DEBUG]) as fp:
    for line in fp:
        inp.append([int(x) for x in line.strip()])


def part1():
    count = 0
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            neighbours = []
            # Go Up
            if y > 0:
                neighbours.append(inp[y - 1][x])
            # Go Down
            if y < len(inp) - 1:
                neighbours.append(inp[y + 1][x])
            # Go Left
            if x > 0:
                neighbours.append(inp[y][x - 1])
            # Go Right
            if x < len(inp[y]) - 1:
                neighbours.append(inp[y][x + 1])
            # Is the current element the smallest amongst its neighbours?
            if inp[y][x] < min(neighbours):
                count += inp[y][x] + 1
    return count


def part2():
    sizes = []
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] not in (-1, 9):
                sizes.append(dfs(x, y))
    sizes.sort()
    sizes.reverse()
    return sizes[0] * sizes[1] * sizes[2]


def dfs(x, y):
    count = 1
    inp[y][x] = -1  # -1 => visited
    if y > 0 and inp[y - 1][x] not in (-1, 9):  # Go up
        count += dfs(x, y - 1)
    if y < len(inp) - 1 and inp[y + 1][x] not in (-1, 9):  # Go down
        count += dfs(x, y + 1)
    if x > 0 and inp[y][x - 1] not in (-1, 9):  # Go left
        count += dfs(x - 1, y)
    if x < len(inp[y]) - 1 and inp[y][x + 1] not in (-1, 9):  # Go right
        count += dfs(x + 1, y)

    return count


print(part1())
print(part2())
