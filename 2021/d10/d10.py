#!/usr/bin/env python3

# 1: Use test input
# 0: Use final input
DEBUG = 0
filename = ["inp.txt", "inp-test.txt"]

inp = []
with open(filename[DEBUG]) as fp:
    for line in fp:
        inp.append(line.strip())

brackets = {"[": "]", "(": ")", "{": "}", "<": ">"}


def part1(arr):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    result = []
    for row in arr:
        stack = []
        for c in row:
            if c in brackets.keys():
                stack.append(c)
            elif c in brackets.values():
                p = stack.pop()
                if c != brackets[p]:  # Found the corresponding match
                    result.append(scores[c])
    return sum(result)


def part2(arr):
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    result = []
    for row in arr:
        stack = []
        for c in row:
            if c in brackets.keys():
                stack.append(c)
            elif c in brackets.values():
                p = stack.pop()
                if c != brackets[p]:  # Corrupted line, skip
                    stack = []
                    break

        if len(stack) == 0:
            continue

        intermediate_score = 0
        stack.reverse()
        for x in stack:
            intermediate_score = intermediate_score * 5 + scores[brackets[x]]
        result.append(intermediate_score)

    result.sort()
    return result[len(result) // 2]


print(part1(inp))
print(part2(inp))
