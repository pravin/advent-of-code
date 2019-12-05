#!/usr/bin/env python3

class Day04:
    def partA(self):
        count = 0
        for p in range(246540, 787420):
            s = str(p)
            adjacent_same = False
            non_decreasing = True
            for i in range(len(s) - 1):
                if s[i] > s[i+1]:
                    non_decreasing = False
                    break
                if s[i] == s[i+1]:
                    adjacent_same = True

            if non_decreasing and adjacent_same:
                count += 1
        return count

    def partB(self):
        count = 0
        for p in range(246540, 787420):
            s = str(p)
            contains_two = False
            m = {x: s.count(x) for x in set(s)}
            if 2 in m.values():
                contains_two = True
            
            non_decreasing = True
            for i in range(len(s) - 1):
                if s[i] > s[i+1]:
                    non_decreasing = False
                    break

            if non_decreasing and contains_two:
                count += 1
        return count

if __name__ == '__main__':
    d = Day04()
    print("Part A", d.partA())
    print("Part B", d.partB())