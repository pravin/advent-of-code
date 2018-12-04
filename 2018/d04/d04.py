#!/usr/bin/env python3

class Day04:
    guard_map = {}

    def __init__(self):
        guard_id = 0
        state = 0 # 0: Awake, 1: Asleep
        pos = 0
        with open('sorted_input.txt') as fp:
            for line in fp:
                minute = int(line[15:17])
                if line[19] == 'G':
                    guard_id = int(line[26:].split(' ')[0])
                    if not guard_id in self.guard_map:
                        self.guard_map[guard_id] = [0] * 60
                elif line[19] == 'f': # Falls asleep
                    if state == 0: # If Guard was awake, state changes
                        pos = minute
                        state = 1
                elif line[19] == 'w':
                    if state == 1: # If guard was asleep, state changes
                        for i in range(pos, minute):
                            self.guard_map[guard_id][i] += state
                        pos = minute
                        state = 0
    
    def puzzle1(self):
        max_sum = 0
        best_minute = -1
        selected_id = -1
        for k, v in self.guard_map.items():
            if sum(v) > max_sum:
                max_sum = sum(v)
                selected_id = k
                best_minute = v.index(max(v))

        return selected_id * best_minute


    def puzzle2(self):
        max_sum = 0
        selected_id = -1
        best_minute = -1
        for k, v in self.guard_map.items():
            if max(v) > max_sum:
                max_sum = max(v)
                best_minute = v.index(max(v))
                selected_id = k
        return selected_id * best_minute



if __name__ == '__main__':
    d = Day04()
    print(d.puzzle1())
    print(d.puzzle2())