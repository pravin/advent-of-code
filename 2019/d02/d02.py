#!/usr/bin/env python3

class Day02:
    def partA(self, input_list):
        ptr = 0
        while ptr < len(input_list):
            if ptr + 3 < len(input_list):
                opcode, num1, num2, output = input_list[ptr:ptr+4]
                if opcode == 1:
                    input_list[output] = input_list[num1] + input_list[num2]
                elif opcode == 2:
                    input_list[output] = input_list[num1] * input_list[num2]
                else:
                    assert opcode == 99
                    return input_list
                ptr += 4
            else:
                opcode = input_list[ptr]
                assert opcode == 99
                return input_list

    def partB(self, input_list):
        for noun in range(100):
            for verb in range(100):
                input_list[1] = noun
                input_list[2] = verb
                value = self.partA(input_list[:])[0]
                if value == 19690720:
                    return 100 * noun + verb


if __name__ == '__main__':
    input_list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]
    d = Day02()
    # Read the instructions at the end!
    input_list[1] = 12
    input_list[2] = 2
    print("Part A", d.partA(input_list[:])[0])
    print("Part B", d.partB(input_list[:]))