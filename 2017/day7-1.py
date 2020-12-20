#!/usr/bin/env python

import re

valid = 0
c = 0
for line in open("input7.txt", "r"):
    c += 1
    matches = re.findall(r'(.)(.)\2\1', line)
    wrong = None
    for m in matches:
        if m[0] == m[1]:
            continue
        abba = m[0] + m[1] + m[1] + m[0]
        wrong_match = re.match(r'.*\[[^\]]*{}[^\]]*\].*'.format(abba), line)
        if wrong_match:
            wrong = True
            break
        else:
            wrong = False
    if wrong == False:
        valid += 1

print(valid)

