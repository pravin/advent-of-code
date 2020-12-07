#!/usr/bin/env python3

passports = []
data = {}
with open('input.txt') as fp:
    for line in fp:
        if line.strip() == '':
            passports.append(data)
            data = {}
            continue
        kv_pairs = line.split()
        for kv in kv_pairs:
            k, v = kv.split(':')
            data[k] = v

    passports.append(data)

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def common(skip):
    num_valid = 0
    for p in passports:
        is_valid = True
        for f in fields:
            if not (f in p and isFieldValid(f, p[f], skip)):
                is_valid = False
                break
        if is_valid:
            num_valid += 1
    return num_valid

def isFieldValid(field, value, skip):
    if skip: return True
    response = False
    if field == 'byr':
        v = int(value)
        response = v >= 1920 and v <= 2002
    elif field == 'iyr':
        v = int(value)
        response = v >= 2010 and v <= 2020
    elif field == 'eyr':
        v = int(value)
        response = v >= 2020 and v <= 2030
    elif field == 'hgt':
        v = int(value[:-2])
        if value.endswith('cm'):
            response = v >= 150 and v <= 193
        elif value.endswith('in'):
            response = v >= 59 and v <= 76
    elif field == 'hcl':
        if value[0] == '#' and len(value) == 7:
            try:
                int(value[1:], 16)
                response = True
            except:
                response = False
    elif field == 'ecl':
        response = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field == 'pid':
        response = value.isnumeric() and len(value) == 9
    return response

        

def part1():
    return common(True)

def part2():
    return common(False)

print(part1())
print(part2())
