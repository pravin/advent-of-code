#!/usr/bin/env python3

inp = []
max_x, max_y = 0, 0

with open('05.txt') as fp:
    for line in fp:
        line = line.replace(' -> ', ',').strip()
        x1, y1, x2, y2 = list(map(lambda x: int(x), line.split(',')))
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
        inp.append((x1, y1, x2, y2))
    max_x += 1
    max_y += 1

def part1(arr):
    mat = [[0 for j in range(max_x)] for i in range(max_y)] # access using mat[x][y]
    for x1, y1, x2, y2 in arr:
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2+1): # co-ordinate, need to capture endpoint
                mat[y][x1] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1): # co-ordinate, need to capture endpoint
                mat[y1][x] += 1
    numsum = 0
    for list1 in mat:
        numsum += len(list(filter(lambda x: x > 1, list1)))
    return numsum, mat

def part2(arr, mat):
    for x1, y1, x2, y2 in arr:
        if x1 != x2 and y1 != y2:
            step_x = 1 if x2 > x1 else -1
            step_y = 1 if y2 > y1 else -1
            numsteps = (x2 - x1) * step_x + 1
            for i in range(numsteps):
                mat[y1 + step_y*i][x1 + step_x*i] += 1
        
    numsum = 0
    for list1 in mat:
        numsum += len(list(filter(lambda x: x > 1, list1)))
    return numsum

part1result, arr1 = part1(inp)
print(part1result)
print(part2(inp, arr1))
