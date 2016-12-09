#!/usr/bin/env python

import re

data = str(open("input9.txt", "r").read().strip())

def rec(data, amount):
    length = 0
    i = 0
    while i < len(data):
        if data[i] != '(':
            length += 1
            i += 1
            continue
        else:
            num, amt = re.search(r"\(([0-9]+x[0-9]+)\)", data[i:]).group(1).split("x")
            i += len(num) + len(amt) + 3
            length += rec(data[i:i+int(num)], int(amt))
            i += int(num)
    return length*amount

print(rec(data, 1))
