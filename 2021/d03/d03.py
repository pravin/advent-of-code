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
    print(acc)
    gamma = list(map(lambda x: '1' if x > len(arr)/2 else '0', acc))
    epsilon = list(map(lambda x: '1' if x == '0' else '0', gamma))
    return int(''.join(gamma), 2), int(''.join(epsilon), 2)

def part2(arr):
    gamma, epsilon = part1(inp)

    return

gamma, epsilon = part1(inp)
print(gamma * epsilon)
print(part2())