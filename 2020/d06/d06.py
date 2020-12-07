#!/usr/bin/env python3


def part1():
    d = set()
    data = []
    with open('input.txt') as fp:
        for line in fp:
            if line.strip() == '':
                data.append(d)
                d = set()
            else:
                d = d.union(line.strip())
    data.append(d)
    return sum(len(d) for d in data)

def part2():
    d = set()
    data = []
    newlineflag = True
    with open('input.txt') as fp:
        for line in fp:
            if line.strip() == '':
                data.append(d)
                d = set()
                newlineflag = True
            else:
                if newlineflag:
                    d = set(line.strip())
                else:
                    d = d.intersection(line.strip())
                newlineflag = False
    data.append(d)
    return sum(len(d) for d in data)

print(part1())
print(part2())