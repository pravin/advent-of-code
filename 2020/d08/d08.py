#!/usr/bin/env python3

data = []
visited = []
with open('input.txt') as fp:
    for line in fp:
        ins, val = line.strip().split(' ')
        data.append([ins, int(val)])
        visited.append(0)

def part1():
    pos = 0
    acc = 0
    while True:
        if pos >=len(data): break
        ins, val = data[pos]
        if visited[pos] != 0: # Visited this already
            return pos, acc
        visited[pos] = 1 # Mark as visited
        
        if ins == 'jmp':
            pos += val
        elif ins == 'acc':
            acc += val
            pos += 1
        elif ins == 'nop':
            pos += 1
    return pos, acc

def part2():
    global visited
    for i in range(len(data)):
        if data[i][0] == 'nop':
            data[i][0] = 'jmp'
        elif data[i][0] == 'jmp':
            data[i][0] = 'nop'
        visited = [0] * len(data)
        p, a = part1()
        if p >= len(data):
            return a
        
        if data[i][0] == 'nop':
            data[i][0] = 'jmp'
        elif data[i][0] == 'jmp':
            data[i][0] = 'nop'  
    return -1

print(part1()[1])
print(part2())