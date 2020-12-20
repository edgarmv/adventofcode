#!/usr/bin/python3

import sys
from queue import Queue

def floodfill(grid, q, visited):
    while q.qsize() > 0:
        x, y, distance = q.get()
        if x >= len(grid[0]) or y >= len(grid) or x < 0 or y < 0 or (x,y) in visited:
            continue
        print(len(visited))
        grid[y][x] = distance
        visited.append((x, y))
        if (x+1,y+0) not in visited:
            q.put((x+1, y+0, distance+1))
        if (x-1,y+0) not in visited:
            q.put((x-1, y+0, distance+1))
        if (x+0,y+1) not in visited:
            q.put((x+0, y+1, distance+1))
        if (x+0,y-1) not in visited:
            q.put((x+0, y-1, distance+1))


def main(argc, argv):
    if argc < 2:
        print("Usage: ./day6 <filename>")
        sys.exit(1)

    coordinates = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in open(argv[1], "r").readlines()]
    minx = min(x[0] for x in coordinates)
    miny = min(x[1] for x in coordinates)
    maxx = max(x[0] for x in coordinates)
    maxy = max(x[1] for x in coordinates)

    print(coordinates)
    print(minx, miny, maxx, maxy)

    grid = [[-1 for x in range(minx, maxx+1)] for y in range(miny, maxy+1)]

    x, y = coordinates[0]
    q = Queue()
    q.put((x-minx, y-miny, 0))
    floodfill(grid, q, [])


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
