#!/usr/bin/env python

discs = []

for line in open("input15.txt"):
    pos = int(line.split()[3])
    start = int(line.split()[11][:-1])
    discs.append([pos, start])

discs.append([11, 0])

t = 0
while True:
    if all(disc[1] == (disc[0] - (i+1)) % disc[0] for i, disc in enumerate(discs)):
        print(t)
        break

    for disc in discs:
        disc[1] = (disc[1] + 1) % disc[0]

    t += 1
