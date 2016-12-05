#!/usr/bin/env python

possible = 0

for line in open("input3.txt", "r"):
    numbers = list(map(int, line.split()))
    if (numbers[0] + numbers[1] > numbers[2]
        and numbers[0] + numbers[2] > numbers[1]
        and numbers[1] + numbers[2] > numbers[0]):

        possible += 1

print(possible)
