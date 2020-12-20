#!/usr/bin/env python3

mass = sum(int(x.strip()) // 3 - 2 for x in open('day1.txt').readlines())
print("Solution 1:", mass)

mass = 0
for line in [int(x.strip()) for x in open('day1.txt').readlines()]:
    fuel = (line // 3) - 2
    while fuel > 0:
        mass += fuel
        fuel = (fuel // 3) - 2

print("Solution 2:", mass)
