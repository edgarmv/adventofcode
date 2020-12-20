#!/usr/bin/env python

moves = [x.strip() for x in open("input1.txt", "r").read().split(',')]

locations = set()
x = 0
y = 0
direction = 0
locations.add((x,y))

def make_move(_x, _y):
    global locations, x, y
    for i in range(int(move[1:])):
        y += 1 * _y
        x += 1 * _x
        if (x,y) in locations:
            print(abs(x) + abs(y))
            exit(0)
        locations.add((x,y))

for move in moves:
    if move[0] == 'R':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    
    if direction == 0:
        make_move(0, 1)
    elif direction == 1:
        make_move(1, 0)
    elif direction == 2:
        make_move(0, -1)
    else:
        make_move(-1, 0)
