#!/usr/bin/env python3


def inputdata():
    data = []
    with open('input.txt') as fp:
        for line in fp:
            data.append(list(line.strip('\n')))
    return data


# Find the starting point
def findstart(data):
    START_SYMBOLS = ['|', '-']
    w, h = len(data[0]), len(data)
    for i in range(w):  # Top and bottom lines
        if data[0][i] in START_SYMBOLS:
            return (i, 0)
        if data[w - 1][i] in START_SYMBOLS:
            return (i, w - 1)
    for i in range(h):  # Left and right edges
        if data[i][0] in START_SYMBOLS:
            return (0, i)
        if data[i][h - 1] in START_SYMBOLS:
            return (h - 1, i)


def traverse(data, curx, cury, dirx, diry):
    SYMBOLS = ['|', '-']
    retval = []
    steps = 0
    while True:
        elm = data[cury][curx]
        if elm in SYMBOLS or elm.isalpha():
            if elm.isalpha():
                retval.append(elm)
            curx += dirx
            cury += diry
            steps += 1
        elif elm == '+':  # Find direction of travel
            for (x, y) in [(diry, dirx), (diry * -1, dirx * -1)]:
                elm = data[cury + y][curx + x]
                if elm in SYMBOLS or elm.isalpha():
                    dirx, diry = x, y
                    curx += dirx
                    cury += diry
                    steps += 1
        else:
            break
    return retval, steps


if __name__ == '__main__':
    data = inputdata()
    curx, cury = findstart(data)
    # Cheated with the dirx/diry as I know the start direction from the input
    retval, steps = traverse(data, curx, cury, 0, 1)
    print(''.join(retval), steps)

