#!/usr/bin/env python3

valid_sum_part1 = 0
valid_sum_part2 = 0
with open('input.txt', 'r') as fp:
    for line in fp:
        words = line.split()
        words.sort()
        # Part 1
        dup_part1 = False
        for i in xrange(len(words)-1):
            if words[i] == words[i+1]:
                dup_part1 = True
        if not dup_part1:
            valid_sum_part1 += 1
        
        # Part 2
        dup_part2 = False
        words = [sorted(x) for x in words] # Anagrams will have the same characters
        words.sort()
        for i in xrange(len(words)-1):
            if words[i] == words[i+1]:
                dup_part2 = True
        if not dup_part2:
            valid_sum_part2 += 1

print(valid_sum_part1)
print(valid_sum_part2)