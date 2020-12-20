#!/usr/bin/env python3

def calculate_output(integers, noun, verb):
    integers = list(integers)
    integers[1] = noun
    integers[2] = verb

    index = 0
    while integers[index] != 99:
        if integers[index] == 1:
            integers[integers[index+3]] = integers[integers[index+1]] + integers[integers[index+2]]
        elif integers[index] == 2:
            integers[integers[index+3]] = integers[integers[index+1]] * integers[integers[index+2]]
        elif integers[index] == 3:
            integers[integers[index+3]] = integers[integers[index+1]] * integers[integers[index+2]]
        index += 4

    return integers[0]

integers = [int(x.strip()) for x in open('day2.txt').read().split(',')]

solution1 = calculate_output(integers, 12, 2)
print("Solution 1:", solution1)

for noun in range(1, 100):
    for verb in range(1, 100):
        output = calculate_output(integers, noun, verb)
        if output == 19690720:
            print("Solution 2:", 100 * noun + verb)


