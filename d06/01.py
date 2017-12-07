#!/usr/bin/env python3

bank = [0, 2, 7, 0]
bank = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
visited = {}
steps = 0

l = len(bank)
while tuple(bank) not in visited:
    visited[tuple(bank)] = steps
    m = max(bank)
    i = bank.index(m)
    bank[i] = 0 # Set the item to 0
    quotient = m // l

    bank = [x + quotient for x in bank] # Evenly distribute quotient
    remainder = m % l
    arr = [1] * (remainder) + [0] * (l - remainder)
    arr = arr[-i-1:] + arr[:-i-1]

    bank = [x+y for x, y in zip(bank, arr)]
    steps += 1

    
print (steps, steps - visited[tuple(bank)]) # Step1, Step2