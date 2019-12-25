#!/usr/bin/env python3

import copy

class Day24:
    def partA(self, state):
        new_state = copy.deepcopy(state)
        directions = [
            [-1, 0], # N
            [1, 0], # S
            [0, -1], # W
            [0, 1], # E
            #[-1, -1], # NW
            #[1, -1], # SW
            #[-1, 1], # NE
            # [-1, -1], # SE
        ]

        for x in range(len(state[0])):
            for y in range(len(state)):
                adjacent_count = 0
                for cy, cx in directions:
                    cy = cy + y
                    cx = cx + x
                    if cy >= 0 and cy < len(state) and \
                        cx >= 0 and cx < len(state[0]):
                        if state[cy][cx] == 1:
                            adjacent_count += 1
                #print x, y, state[y][x], adjacent_count

                if adjacent_count == 1 and state[y][x] == 1:
                    new_state[y][x] = 1
                elif adjacent_count in (1, 2) and state[y][x] == 0:
                    new_state[y][x] = 1
                else:
                    new_state[y][x] = 0
        return new_state
    
    def list2string(self, the_list):
        return ''.join([str(item) for sublist in the_list for item in sublist])

if __name__ == '__main__':
    hashmap = {}
    d = Day24()
    res = [
        [1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0],
    ]
    hashmap[d.list2string(res)] = 1
    repeated = None
    while True:
        res = d.partA(res)
        dres = d.list2string(res)
        if dres in hashmap:
            repeated = res
            break
        else:
            hashmap[dres] = 1
    
    flatlist = [num for sublist in repeated for num in sublist]
    
    print(sum(map(lambda x, y: x * y, flatlist, [2**i for i in range(25)])))
