#!/usr/bin/env python

LINE_LEN = 8
occ = [[0] * 26 for _ in xrange (LINE_LEN)]

with open('d06.in') as fp:
    for line in fp:
        count = 0
        for c in line.strip():
            idx = ord(c) - ord('a')
            occ[count][idx] += 1
            count += 1

ar = []
ar2 = []
for i in range(LINE_LEN):
    ar.append(chr(occ[i].index(max(occ[i])) + ord('a')))
    ar2.append(chr(occ[i].index(min(occ[i])) + ord('a')))

print "Step1", ''.join(ar)
print "Step2", ''.join(ar2)