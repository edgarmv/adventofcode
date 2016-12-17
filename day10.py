#!/usr/bin/env python

commands = []

bots = [[] for x in range(300)]
outputs = [[] for x in range(300)]

def distribute():
    distrubuted = False
    for cmd in commands:
        bot = int(cmd.split()[1])
        if len(bots[bot]) == 2:
            if 61 in bots[bot] and 17 in bots[bot]:
                print("Answer 1:", bot)
            h, l = max(bots[bot]), min(bots[bot])
            low_to = int(cmd.split()[6])
            high_to = int(cmd.split()[11])

            if cmd.split()[5] == 'output':
                outputs[low_to].append(l)
            else:
                bots[low_to].append(l)
            if cmd.split()[10] == 'output':
                outputs[high_to].append(h)
            else:
                bots[high_to].append(h)

            bots[bot] = []
            commands.remove(cmd)
            distrubuted = True
    return distrubuted


for line in open("input10.txt", "r"):
    if "goes" in line:
        bot = int(line.split()[5])
        value = int(line.split()[1])
        bots[bot].append(value)
        while distribute():
            pass
    else:
        bot = int(line.split()[1])
        if len(bots[bot]) == 2:
            h, l = max(bots[bot]), min(bots[bot])
            low_to = int(line.split()[6])
            high_to = int(line.split()[11])
            bots[low_to].append(l)
            bots[high_to].append(h)
            while distribute():
                pass
        else:
            commands.append(line)

print("Answer 2:", outputs[0][0] * outputs[1][0] * outputs[2][0])
