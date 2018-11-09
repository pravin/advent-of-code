#!/usr/bin/env python3

# Part 1
with open('input.txt', 'r') as fp:
    sum = 0
    for line in fp:
        row = [int(x) for x in line.split()]
        max_val = max(row)
        min_val = min(row)
        sum += max_val - min_val
    print(sum)

# Part 2
with open('input.txt', 'r') as fp:
    sum = 0
    for line in fp:
        row = [int(x) for x in line.split()]
        row.sort()
        for i in xrange(len(row)-1):
            for j in xrange(i+1, len(row)):
                if row[j] % row[i] == 0:
                    sum += row[j] / row[i]
    print(sum)
