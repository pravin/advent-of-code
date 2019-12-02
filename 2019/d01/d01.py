#!/usr/bin/env python3

class Day01:
    def readFile(self, filename):
        module_list = []
        with open(filename) as fp:
            for line in fp:
                module_list.append(int(line.strip()))
        return module_list

    def partA(self, module_list):
        fuel_needed = 0
        for item in module_list:
            fuel_needed += item // 3 - 2
        return fuel_needed

    def partB(self, module_list):
        new_list = []
        fuel_needed = 0
        for item in module_list:
            fuel_needed_for_this_item = item // 3 - 2
            if fuel_needed_for_this_item > 0:
                fuel_needed += fuel_needed_for_this_item
                if fuel_needed_for_this_item > 0:
                    new_list.append(fuel_needed_for_this_item)
            
        if len(new_list) > 0:
            fuel_needed += self.partB(new_list)
        return fuel_needed

if __name__ == '__main__':
    d = Day01()
    module_list = d.readFile('in.txt')
    print("Part A:", d.partA(module_list))
    print("Part B:", d.partB(module_list))