#!/usr/bin/env python

possible = 0

f = open("input3.txt", "r")

for line in f:
    line1 = list(map(int, line.split()))
    line2 = list(map(int, f.readline().split()))
    line3 = list(map(int, f.readline().split()))

    if (line1[0] + line2[0] > line3[0]
        and line1[0] + line3[0] > line2[0]
        and line2[0] + line3[0] > line1[0]):

        possible += 1

    if (line1[1] + line2[1] > line3[1]
        and line1[1] + line3[1] > line2[1]
        and line2[1] + line3[1] > line1[1]):

        possible += 1

    if (line1[2] + line2[2] > line3[2]
        and line1[2] + line3[2] > line2[2]
        and line2[2] + line3[2] > line1[2]):

        possible += 1
print(possible)
