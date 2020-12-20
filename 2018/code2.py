#!/usr/bin/python3

import sys
from collections import Counter

def main(argc, argv):
    if argc < 2:
        print("Usage: ./code2 <filename>")
        sys.exit(1)

    boxids = [l.strip() for l in open(argv[1], "r").readlines()]

    twos = 0
    threes = 0

    for boxid in boxids:
        counter = Counter(boxid).most_common()
        twos += 1 if any(x[1] == 2 for x in counter) else 0
        threes += 1 if any(x[1] == 3 for x in counter) else 0

    print("Chechsum: {}".format(twos*threes))

    for i in range(len(boxids)):
        for j in range(i+1, len(boxids)):
            if sum(1 if boxids[i][x] != boxids[j][x] else 0 for x in range(len(boxids[i]))) == 1:
                string = "".join(boxids[i][x] if boxids[j][x] == boxids[i][x] else "" for x in range(len(boxids[i])))
                print("Common letters: {}".format(string))
                sys.exit(0)


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
