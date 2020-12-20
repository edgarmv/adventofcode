#!/usr/bin/env python

f = open("input2.txt", "r")

keypad = [[ 0,   0,  '1',  0,   0],
          [ 0,  '2', '3', '4',  0],
          ['5', '6', '7', '8', '9'],
          [ 0,  'A', 'B', 'C',  0],
          [ 0,   0,  'D',  0,   0]]
x = 1
y = 1

solution = []

for line in f:
    for char in line.strip():
        if char == 'L' and (x-1) >= 0 and keypad[y][x-1] != 0:
            x -= 1
        if char == 'R' and (x+1) <= 4 and keypad[y][x+1] != 0:
            x += 1
        if char == 'D' and (y+1) <= 4 and keypad[y+1][x] != 0:
            y += 1
        if char == 'U' and (y-1) >= 0 and keypad[y-1][x] != 0:
            y -= 1
    solution.append(keypad[y][x])

print(solution)

