#!/usr/bin/env python3

class Day05:

    def puzzle1(self):
        polymer = ''
        with open('input.txt') as fp:
            polymer = fp.read().strip()
        return len(self.reduce(list(polymer)))

    def reduce(self, str):
        print('.')
        prev_len = len(str)
        while True:
            pos = 0
            while pos < len(str)-1:
                c1, c2 = str[pos], str[pos+1]
                if c1 != c2 and c1.lower() == c2.lower():
                    str = str[:pos] + str[pos+2:]
                else:
                    pos += 1

            if len(str) == prev_len:
                break
            prev_len = len(str)
        return str

    def puzzle2(self):
        polymer = ''
        with open('input.txt') as fp:
            polymer = fp.read().strip()

        chars = set(polymer.lower())
        return min(map(lambda c: len(self.reduce(list(polymer.replace(c, '').replace(c.upper(), '')))), chars))


if __name__ == '__main__':
    d = Day05()
    print(d.puzzle1())
    print(d.puzzle2())
