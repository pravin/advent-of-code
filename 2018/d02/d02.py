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
        for i in range(len(self._input) - 1):
            for j in range(i, len(self._input)):
                diff = self.edit_d(self._input[i], self._input[j])
                if len(diff) == 1:
                    return self._input[i][:diff[0]] + self._input[i][diff[0]+1:]

        return None

    def edit_d(self, str1, str2):
        """ Assumption: len(str1) == len(str2) """
        diff = []
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff.append(i)
        return diff



if __name__ == '__main__':
    d = Day02()
    print(d.puzzle1())
    print(d.puzzle2())

                
