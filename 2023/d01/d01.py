#!/usr/bin/env python3

import re

def part1():
    _sum = 0
    with open("01.txt") as fp:
        for line in fp:
            numbers = re.sub(r"[a-z]", "", line.strip())
            _sum += int(numbers[0] + numbers[-1])

    print(_sum)

def part2():
    _sum = 0
    numwords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open("01.txt") as fp:
        for line in fp:
            line = line.strip()
            firstnum = [line.find(x) for x in numwords]
            min_index = -1
            for i in range(len(firstnum)):
                if firstnum[i] >= 0:
                    if min_index == -1:
                        min_index = i
                    elif firstnum[i] < firstnum[min_index]:
                        min_index = i
                    
                        
            if min_index >= 0:
                line = line.replace(numwords[min_index], str(min_index + 1))
            
            lastnum = [line.rfind(x) for x in numwords]
            max_index = lastnum.index(max(lastnum))
            if max_index >= 0:
                line = line.replace(numwords[max_index], str(max_index + 1))
            
            numbers = re.sub(r"[a-z]", "", line)
            _sum += int(numbers[0] + numbers[-1])

    print(_sum)

if __name__ == '__main__':
    part1()
    part2()
