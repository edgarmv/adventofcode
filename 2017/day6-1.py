#!/usr/bin/env python

from collections import Counter

print("".join(list(Counter("".join(x)).most_common(1)[0][0] for x in zip(*[y.replace('\n', '') for y in open("input6.txt", "r")]))))
