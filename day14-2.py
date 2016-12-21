#!/usr/bin/env python

import hashlib
import re

hash_key = "yjdafjpo"

possible_keys = set()
keys_found = 0
keys = []

for num in range(1000000):
    keynum = (hash_key + str(num))
    h = keynum
    for i in range(2017):
        h = hashlib.md5(h.encode("utf-8")).hexdigest().lower()

    match = re.search(r"([a-z0-9])\1\1", h) 

    tmp = set()

    for key in possible_keys:
        if key[1] + 1000 < num:
            continue

        match5 = re.search(r"({})\1\1\1\1".format(key[0]), h)
        if match5:
            keys_found += 1
            keys.append(key[1])
        else:
            tmp.add(key)

    if keys_found >= 64:
        print(sorted(keys)[63])
        break

    possible_keys = tmp

    if match:
        possible_keys.add((match.group()[0], num))
