#!/usr/bin/env python3

from pprint import pprint

boards = []
order = []

# 1: Use test input
# 0: Use final input
DEBUG = 1
filename = ["inp.txt", "inp-test.txt"]

with open(filename[DEBUG]) as fp:
    firstline = False
    numbers = []
    for line in fp:
        if line.strip() == '':
            if len(numbers) > 0:
                boards.append(numbers)
                numbers = []
            continue
        if not firstline:
            firstline = True
            order = [int(x) for x in line.split(",")]
        else:
            numbers.append([int(x) for x in line.strip().split()])
    boards.append(numbers)

def part1():
    for n in order:
        for board in boards:
            for row in board:
                for itm in row:
                    if itm == n:
                        itm = -1
        bingo = check_bingo()
        if bingo is not None:
            return bingo
    return None

