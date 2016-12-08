#!/usr/bin/env python

screen = [["." for i in range(50)] for j in range(6)]

def rotate(l, n):
    return  l[-n:] + l[:-n]


c = 0
for line in open("input8.txt", "r"):
    c += 1
    ins = line.split() 
    if ins[0] == 'rect':
        cord = ins[1].split("x")
        for i in range(int(cord[0])):
            for j in range(int(cord[1])):
                screen[j][i] = '#'
    elif ins[0] == 'rotate' and ins[1] == 'column':
        cord = int(ins[2].split("=")[1])
        by = int(ins[4])
        l = [screen[x][cord] for x in range(6)]
        n = rotate(l, by)
        for i in range(6):
            screen[i][cord] = n[i]

    elif ins[0] == 'rotate' and ins[1] == 'row':
        cord = int(ins[2].split("=")[1])
        by = int(ins[4])
        l = screen[cord]
        n = rotate(l, by)
        screen[cord] = n


for line in screen:
    print("".join(line))

print(sum(l.count("#") for l in screen))
