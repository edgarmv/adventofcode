#!/usr/bin/env python3

wires = [x.strip().split(',') for x in open('day3.txt').readlines()]
directions = { 'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0) }
grid = set((0,0))

def manhattan(t):
    return sum(abs(x) for x in t)

def crossing_wires(wires, crossing=False):
    index = (0, 0)
    crosses = set()
    for path in wires:
        direction = path[0]
        distance = int(path[1:])
        for i in range(distance):
            index = tuple(map(sum, zip(index, directions[direction])))
            if index in grid:
                crosses.add(index)
            if crossing == False:
                grid.add(index)
    return crosses

def shortest_path(wires, crosses):
    distances = dict()
    index = (0, 0)
    d = 0

    for path in wires:
        direction = path[0]
        distance = int(path[1:])
        for i in range(distance):
            d += 1
            index = tuple(map(sum, zip(index, directions[direction])))
            if index in crosses:
                distances[index] = d
    return distances


crossing_wires(wires[0])
crosses = crossing_wires(wires[1], crossing=True)

solution1 = min(manhattan(x) for x in crosses)
print("Solution 1:", solution1)

wire0_steps = shortest_path(wires[0], crosses)
wire1_steps = shortest_path(wires[1], crosses)

solution2 = min(wire0_steps[key] + wire1_steps[key] for key in crosses)
print("Solution 2:", solution2)
