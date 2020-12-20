#!/usr/bin/env python

from collections import Counter
import re

sector_sum = 0

for line in open("input4.txt", "r"):
    name, sector, checksum = re.match('([\D\-]+)-([\d]+)\[(.*)\]', line).group(1,2,3)
    correct_checksum = "".join(i[0] for i in sorted(Counter(name.replace("-", "")).most_common(), key=lambda x: (-x[1], x[0]))[:5])

    if (correct_checksum == checksum):
        sector_sum += int(sector)

print(sector_sum)
