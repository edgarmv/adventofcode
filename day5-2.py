#!/usr/bin/env python

from hashlib import md5

code = "cxdnnyjw"
password = [None]*8
counter = 0

while True:
    md5_hash = md5(bytes(code + str(counter), encoding='utf-8')).hexdigest()
    if md5_hash[:5] == '00000':
        if md5_hash[5].isdigit():
            position = int(md5_hash[5])
            if position < 8 and password[position] == None:
                password[position] = md5_hash[6]
            if all(x != None for x in password):
                print("".join(password))
                break
    counter += 1
    

