#!/usr/bin/env python

class Day02:
    _input = []
    def __init__(self):
        with open('input.txt') as fp:
            for line in fp:
                self._input.append(line.strip())

    def puzzle1(self): 
        count_array = [0] * 30

        for word in self._input:
            count_map = {}
            for c in list(word):
                count_map[c] = 1 if c not in count_map else count_map[c] + 1
            
            rev_map = dict((v,k) for k,v in count_map.items())
            for k, v in rev_map.items():
                count_array[k] += 1
            
        return count_array[2] * count_array[3]

    def puzzle2(self):
        #sorted_input = sorted([''.join(sorted(list(word))) for word in self._input])
        sorted_input = [set(word) for word in self._input]
        for i in range(len(sorted_input) - 1):
            diff = sorted_input[i+1].symmetric_difference(sorted_input[i])
            if len(diff) < 2:
                return self._input[i+1], self._input[i], diff

        return None


if __name__ == '__main__':
    d = Day02()
    print(d.puzzle1())
    print(d.puzzle2())

                
