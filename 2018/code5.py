#!/usr/bin/python3

import sys
import re
import datetime

def recurs(polymer, start, end):
    if start-1 <= 0 or end +1 >= len(polymer):
        return start, end
    if polymer[start-1].lower() == polymer[end+1].lower() and polymer[start-1] != polymer[end+1]:
        return recurs(polymer, start-1, end+1)
    else:
        return start, end


def main(argc, argv):
    if argc < 2:
        print("Usage: ./code5 <filename>")
        sys.exit(1)

    polymer = list(open(argv[1], "r").read().strip())

    i = 1
    back_index = len(polymer) - 1
    while i <= back_index:
        if polymer[i-1].lower() == polymer[i].lower() and polymer[i-1] != polymer[i]:
            for j in range(i-1, back_index-1):
                polymer[j] = polymer[j+2]
            back_index -= 2
            i -= 1
            continue
        print(back_index)
        i += 1

    print(back_index)


   


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
