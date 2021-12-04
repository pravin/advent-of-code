#!/usr/bin/env python3

inp = []

with open('03.txt') as fp:
    for line in fp:
        inp.append(line.strip())

def part1(arr):
    acc = [0] * len(arr[0])
    for x in arr:
        for i in range(len(x)):
            acc[i] += int(x[i])
    gamma = list(map(lambda x: '1' if x >= len(arr)/2.0 else '0', acc))
    epsilon = list(map(lambda x: '1' if x == '0' else '0', gamma))
    return ''.join(gamma), ''.join(epsilon)

def part2(arr):
    return oxygen(arr) * co2(arr)

def oxygen(arr):
    num_len = len(arr[0])
    for i in range(num_len):
        gamma, epsilon = part1(arr)
        arr = filter(lambda x: x[i] == gamma[i], arr)
        if (len(arr) == 1): break
    retval = int(arr[0], 2)

    return retval

def co2(arr):
    num_len = len(arr[0])
    for i in range(num_len):
        gamma, epsilon = part1(arr)
        arr = filter(lambda x: x[i] == epsilon[i], arr)
        if (len(arr) == 1): break
    retval = int(arr[0], 2)

    return retval

gamma, epsilon = part1(inp)
print(int(gamma, 2) * int(epsilon, 2))
print(part2(inp))