
inp = []

with open('02.txt') as fp:
    for line in fp:
        direction, value = line.split()
        inp.append((direction, int(value)))

def part1(arr):
    x, y = 0, 0
    for direction, val in arr:
        if direction.startswith('f'):
            x += val
        elif direction.startswith('d'):
            y += val
        elif direction.startswith('u'):
            y -= val
        else:
            print("Unexpected")
    return x * y

def part2(arr):
    x, y, aim = 0, 0, 0
    for direction, val in arr:
        if direction.startswith('f'):
            x += val
            y += val * aim
        elif direction.startswith('d'):
            aim += val
        elif direction.startswith('u'):
            aim -= val
        else:
            print("Unexpected")
    return x * y

print(part1(inp))
print(part2(inp))
