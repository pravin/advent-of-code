#!/usr/bin/env python3

from pprint import pprint

# 1: Use test input
# 0: Use final input
DEBUG = 0
filename = ["inp.txt", "inp-test.txt"]

inp, flashed = [], []
ymax, xmax = 0, 0


def get_input():
    global inp, xmax, ymax
    inp = []
    with open(filename[DEBUG]) as fp:
        for line in fp:
            inp.append([int(x) for x in line.strip()])

    ymax, xmax = len(inp) - 1, len(inp[0]) - 1


def flash(x, y):
    inp[y][x] = 0
    flashed[y][x] = 1
    # Go N
    if y > 0 and flashed[y - 1][x] == 0:
        do_increment(x, y - 1)
    # Go NW
    if y > 0 and x > 0 and flashed[y - 1][x - 1] == 0:
        do_increment(x - 1, y - 1)
    # Go NE
    if y > 0 and x < xmax and flashed[y - 1][x + 1] == 0:
        do_increment(x + 1, y - 1)
    # Go W
    if x > 0 and flashed[y][x - 1] == 0:
        do_increment(x - 1, y)
    # Go E
    if x < xmax and flashed[y][x + 1] == 0:
        do_increment(x + 1, y)
    # Go S
    if y < ymax and flashed[y + 1][x] == 0:
        do_increment(x, y + 1)
    # Go SW
    if y < ymax and x > 0 and flashed[y + 1][x - 1] == 0:
        do_increment(x - 1, y + 1)
    # Go SE
    if y < ymax and x < xmax and flashed[y + 1][x + 1] == 0:
        do_increment(x + 1, y + 1)


def do_increment(x, y):
    inp[y][x] += 1
    if flashed[y][x] == 0 and inp[y][x] > 9:
        flash(x, y)


def step():
    global flashed
    flashed = [[0 for x in y] for y in inp]

    for y in range(ymax + 1):
        for x in range(xmax + 1):
            inp[y][x] += 1

    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if flashed[y][x] == 0 and inp[y][x] > 9:
                flash(x, y)

    return sum([sum(x) for x in flashed])


def part1():
    get_input()
    count = 0
    for i in range(100):
        count += step()
    return count


def part2():
    get_input()
    step_counter = 0
    while True:
        step_counter += 1
        count = step()
        if count == (ymax + 1) * (xmax + 1):
            break
    return step_counter


print(part1())
print(part2())
