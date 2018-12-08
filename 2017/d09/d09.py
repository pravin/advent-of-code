#!/usr/bin/env python3

class Day09:
    def part1(self, str):
        p, l = 0, len(str)
        IN_GARBAGE = False
        GRP_COUNTER = 0
        score = 0

        while p < l:
            c = str[p]
            if IN_GARBAGE:
                if c == '>':
                    IN_GARBAGE = False
                elif c == '!':
                    p += 1
            else: # Not in Garbage
                if c == '{':
                    GRP_COUNTER += 1
                elif c == '}':
                    score += GRP_COUNTER
                    GRP_COUNTER -= 1
                elif c == '<':
                    IN_GARBAGE = True
            p += 1
        return score
    
    def part2(self, str):
        

if __name__ == '__main__':
    d = Day09()

    # Test cases
    print(d.part1('{}') == 1)
    print(d.part1('{{{}}}') == 6)
    print(d.part1('{{},{}}') == 5)
    print(d.part1('{{{},{},{{}}}}') == 16)
    print(d.part1('{<a>,<a>,<a>,<a>}') == 1)
    print(d.part1('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9)
    print(d.part1('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9)
    print(d.part1('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3)
    
    with open('d09.txt') as fp:
        s = fp.read()
        print(d.part1(s))
    