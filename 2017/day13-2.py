#!/usr/bin/env python
designer_num = 1362
destination = (31, 39)

def block(x, y):
    num = x*x + 3*x + 2*x*y + y + y*y
    num += designer_num
    num = str(bin(num))[2:].count("1")
    if num % 2 == 0:
        return '.'
    else:
        return '#'

office_size = 50
office = [[block(x, y) for x in range(office_size)] for y in range(office_size)]

positions = [(1,1)]
distances = {(1,1): 0}
visited = set()

i = 0
while i < len(positions):
    x, y = positions[i]
    i += 1

    if distances[(x, y)] == 50:
        continue

    ways = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
    for way in ways:
        if way[0] >= 0 and way[0] < office_size and way[1] >= 0 and way[1] < office_size:
            if way in visited or office[way[1]][way[0]] == '#':
                continue
            positions.append(way)
            distances[way] = distances[(x,y)] + 1
            visited.add(way)

print(len(visited))
