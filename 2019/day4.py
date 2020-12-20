#!/usr/bin/env python3

import itertools

low, high = [int(x) for x in open('day4.txt').read().strip().split('-')]

def two_adjacent(number):
    return any(len(list(g)) >= 2 for _, g in itertools.groupby(str(number)))

def even_adjacent(number):
    return any(len(list(g)) == 2 for _, g in itertools.groupby(str(number)))

def increasing(number):
    digits = [int(x) for x in str(number)]
    return all(digits[i] <= digits[i+1] for i in range(len(digits)-1))

solution1 = 0
solution2 = 0

for i in range(low, high):
    if two_adjacent(i) and increasing(i):
        solution1 += 1
        if even_adjacent(i):
            solution2 += 1

print("Solution 1:", solution1)
print("Solution 2:", solution2)
