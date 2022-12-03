#!/usr/bin/env python3
def part1():
    intersection_list = []
    with open("03.txt") as fp:
        for line in fp:
            line = line.strip()
            mid = len(line) // 2
            first = set(line[:mid])
            second = set(line[mid:])
            intersection_list.append(first.intersection(second).pop())

    the_sum = 0
    for x in intersection_list:
        the_sum += calc_score(x)

    return the_sum


def part2():
    the_sum = 0
    temp_sets = []
    with open("03.txt") as fp:
        for line in fp:
            temp_sets.append(set(line.strip()))
            if len(temp_sets) == 3:
                x = find_common(temp_sets).pop()
                the_sum += calc_score(x)
                temp_sets = []

    return the_sum


def find_common(set_list):
    return set_list[0].intersection(set_list[1].intersection(set_list[2]))


def calc_score(c):
    return (ord(c) - ord("a") + 1) if c.islower() else (ord(c) - ord("A") + 27)


if __name__ == "__main__":
    print(part1())
    print(part2())
