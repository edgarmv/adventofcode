#!/usr/bin/env python

moves = [x.strip() for x in open("input1.txt", "r").read().split(',')]

x = 0
y = 0
direction = 0

for move in moves:
    print(x, y, direction, move)
    if move[0] == 'R':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    
    if direction == 0:
        y += int(move[1:])
    elif direction == 1:
        x += int(move[1:])
    elif direction == 2:
        y -= int(move[1:])
    else:
        x -= int(move[1::])

print(abs(x) + abs(y))
