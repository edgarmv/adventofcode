#!/usr/bin/python3

import sys
import re

def main(argc, argv):
    if argc < 2:
        print("Usage: ./code3 <filename>")
        sys.exit(1)

    grid = [[0 for i in range(1000)] for j in range(1000)]
    lines = open(argv[1], "r").readlines()
    claims = [0] * (len(lines) + 1)

    overlaps = 0


    for line in lines:
        match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
        groups = [int(x) for x in match.groups()]
        idd, x, y, w, h = groups
        
        for i in range(x, x+w):
            for j in range(y, y+h):
                if grid[i][j] == -1:
                    claims[idd] = 1
                    continue
                elif grid[i][j] == 0:
                    grid[i][j] = idd
                else:
                    claims[grid[i][j]] = 1
                    claims[idd] = 1
                    grid[i][j] = -1
                    overlaps += 1

    print("Overlaps: {}".format(overlaps))

    print("Id: {}".format(claims[1:].index(0)+1))



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
