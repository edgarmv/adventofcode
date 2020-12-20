#!/usr/bin/env python

import re

data = open("input9.txt", "r").read().strip()

output = ""

i = 0
while i < len(data):
    if data[i] != '(':
        output += data[i]
        i += 1
        continue

    first = re.search(r"\(([0-9]+x[0-9]+)\)", data[i:]) 
    num = int(first.group(1).split("x")[0])
    amount = int(first.group(1).split("x")[1])
    i += len(first.group(1)) + 2
    for j in range(amount):
        output += data[i:i+num]
    i += num 

print(len(output))
