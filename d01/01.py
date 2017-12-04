#!/usr/bin/env python3

# Common
data = ''
with open('input.txt', 'r') as fp:
    data = fp.read().strip()

length = len(data)

def calc(data, inc):
    sum = 0
    i = 0
    data = data + data[0:inc]
    while i < length:
        if data[i] == data[i+inc]:
            sum += int(data[i])
        i += 1

    return sum

print(calc(data, 1)) # Part 1
print(calc(data, length/2)) # Part 2