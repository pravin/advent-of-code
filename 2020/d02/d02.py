#!/usr/bin/env python3

import re

inp_list = []
with open('input.txt') as fp:
    for line in fp:
        low, high, char, passwd = re.findall(r'(\d+)-(\d+) (\w): (\w+)', line)[0]
        inp_list.append((int(low), int(high), char, passwd))

def part1():
    tot = 0
    for (low, high, char, passwd) in inp_list:
        filteredlist = list(filter(lambda x: x == char, passwd))
        if len(filteredlist) >= low and len(filteredlist) <= high:
            tot += 1
    print(tot)        


def part2():
    tot = 0
    for (p1, p2, char, passwd) in inp_list:
        res1 = passwd[p1-1] == char
        res2 = False
        if p2 <= len(passwd):
            res2 = passwd[p2-1] == char
        if res1 != res2: # Using != as xor operator
            tot += 1 
    print(tot)

part1()
part2()
