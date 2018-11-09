#!/usr/bin/env python3

regmap = {}
maxval = 0
with open('input.txt', 'r') as fp:
    for line in fp:
        multiplier = 1
        changevals = False
        #print(regmap)
        register, operator, value, _, register2, comparator, value2 = line.split()
        if register not in regmap:
            regmap[register] = 0 # initialise to 0
        if operator == 'dec': 
            multiplier = -1
        value = int(value)
        value2 = int(value2)
        if register2 not in regmap:
            regmap[register2] = 0
        if comparator == '>' and regmap[register2] > value2:
            changevals = True
        elif comparator == '>=' and regmap[register2] >= value2:
            changevals = True
        elif comparator == '<' and regmap[register2] < value2:
            changevals = True
        elif comparator == '<=' and regmap[register2] <= value2:
            changevals = True
        elif comparator == '!=' and regmap[register2] != value2:
            changevals = True
        elif comparator == '==' and regmap[register2] == value2:
            changevals = True

        if changevals:
            regmap[register] += value * multiplier
            maxval = max(maxval, regmap[register])
print(max(regmap.values()), maxval)