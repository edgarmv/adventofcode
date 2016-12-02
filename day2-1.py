#!/usr/bin/env python

f = open("input2.txt", "r")

keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
x = 1
y = 1

solution = []

for line in f:
    for char in line.strip():
        if char == 'L':
            x = max(0, x - 1)
        if char == 'R':
            x = min(2, x + 1)
        if char == 'D':
            y = min(2, y + 1)
        if char == 'U':
            y = max(0, y - 1)
    solution.append(keypad[y][x])

print(solution)

