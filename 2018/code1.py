#!/usr/bin/python3

import sys

def main(argc, argv):
    if argc < 2:
        print("Usage: ./code1 <filename>")
        sys.exit(1)

    frequency = 0
    changes = [int(x) for x in open(argv[1], "r").read().split()]
    for change in changes:
        frequency += change

    print("Frequency: {}".format(frequency))

    # Task 2
    frequencies = set()
    frequency = 0
    found = False
    while True:
        for i in range(len(changes)):
            if frequency in frequencies:
                found = True
                break
            else:
                frequencies.add(frequency)
            frequency += changes[i] 
        if found:
            break
    print("Frequency: {}".format(frequency))

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
