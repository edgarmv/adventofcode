#!/usr/bin/env python

import re

print(sum(any(a == c and a != b and b+a+b in h for a, b, c in zip(s, s[1:], s[2:])) for s, h in [(" ".join(line[::2]), " ".join(line[1::2])) for line in [re.split(r'\[([^\]]+)\]', x) for x in open("input7.txt")]]))
