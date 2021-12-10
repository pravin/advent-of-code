#!/usr/bin/env python3

# 1: Use test input
# 0: Use final input
DEBUG = 0
filename = ["09.txt", "09-test.txt"]

inp = []
with open(filename[DEBUG]) as fp:
    for line in fp:
        inp.append([int(x) for x in line.strip()])


def part1(arr):
    count = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            neighbours = []
            # Go Up
            if y > 0:
                neighbours.append(arr[y - 1][x])
            # Go Down
            if y < len(arr) - 1:
                neighbours.append(arr[y + 1][x])
            # Go Left
            if x > 0:
                neighbours.append(arr[y][x - 1])
            # Go Right
            if x < len(arr[y]) - 1:
                neighbours.append(arr[y][x + 1])
            # Is the current element the smallest amongst its neighbours?
            if arr[y][x] < min(neighbours):
                count += arr[y][x] + 1
    return count


def part2(arr):
    pass


print(part1(inp))
