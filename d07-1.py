#!/usr/bin/env python
import re

count = 0
MATCH = r'(\w)(\w)\2\1'

with open('d07.in') as fp:
    for line in fp:
        neg = False
        # Match strings within [] brackets
        for m in re.findall(r'\[(\w*)\]', line): 
            if re.findall(MATCH, m): neg = True

        # If found a neg string, skip
        if neg: continue

        # See if a valid string is found outside [] brackets
        pos = False
        line = re.sub(r'\[(.*?)\]', '-', line.strip())
        for m in re.findall(MATCH, line):
            if m[0] == m[1]: continue # Check if the characters are different
            pos = True

        if pos: count += 1

print count