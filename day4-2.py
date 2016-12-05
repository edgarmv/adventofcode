#!/usr/bin/env python

from collections import Counter
import re

for line in open("input4.txt", "r"):
    name, sector, checksum = re.match('([\D\-]+)-([\d]+)\[(.*)\]', line).group(1,2,3)
    correct_checksum = "".join(i[0] for i in sorted(Counter(name.replace("-", "")).most_common(), key=lambda x: (-x[1], x[0]))[:5])

    if (correct_checksum == checksum):
        if "north" in "".join(chr(((ord(x) - 97 + int(sector)) % 26) + 97) if x != '-' else x for x in name.lower()):
            print(sector)
