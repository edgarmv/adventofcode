#!/usr/bin/env python

from hashlib import md5

code = "cxdnnyjw"
password = ""
counter = 0

while True:
    md5_hash = md5(bytes(code + str(counter), encoding='utf-8')).hexdigest()
    if md5_hash[:5] == '00000':
            password += md5_hash[5]
            if len(password) == 8:
                print(password)
                break
    counter += 1
    

