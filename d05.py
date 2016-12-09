#!/usr/bin/env python
"""
--- Day 5: How About a Nice Game of Chess? ---

You are faced with a security door designed by Easter Bunny engineers that seem
to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time
by finding the MD5 hash of some Door ID (your puzzle input) and an increasing
integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal
representation starts with five zeroes. If it does, the sixth character in the
hash is the next character of the password.

For example, if the Door ID is abc:

The first index which produces a hash that starts with five zeroes is 3231929,
which we find by hashing abc3231929; the sixth character of the hash, and thus
the first character of the password, is 1. 5017308 produces the next interesting
hash, which starts with 000008f82..., so the second character of the password is
8. The third time a hash starts with five zeroes is for abc5278568, discovering
the character f. In this example, after continuing this search a total of eight
times, the password is 18f47a30.

Given the actual Door ID, what is the password?

Your puzzle input is reyedfim.
"""

import md5

found = 0 # Counts how many letters of the password we have found
count = 0 # Increasing counter going into infinity

PASSWORD = 'reyedfim'

step1 = []
step2 = [-1] * 8

while found < 8:
    s = md5.new(PASSWORD + str(count)).hexdigest()
    if s[:5] == '00000':
        print step1, step2
        step1.append(s[5:6])
        try:
            idx, val  = int(s[5:6]), s[6:7]
            if idx < 8:
                if step2[idx] == -1: 
                    found += 1
                    step2[idx] = val
        except:
            pass
    count += 1

print "Step-1", ''.join(step1[:8])
print "Step-2", ''.join(step2)
