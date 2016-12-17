#!/usr/bin/env python

commands = []

bots = []*1000

for line in open("input10.txt", "r"):
    if "goes" in line:
        bot = int(line.split()[5])
        value = int(line.split()[1])
        bots[bot].append(value)
    else:
        bot = int(line.split()[1])
        if len(bots[bot]) == 2:

        else:



