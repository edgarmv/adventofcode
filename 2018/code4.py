#!/usr/bin/python3

import sys
import re
import datetime

def main(argc, argv):
    if argc < 2:
        print("Usage: ./code3 <filename>")
        sys.exit(1)

    lines = open(argv[1], "r").readlines()

    parsed_lines = []

    for line in lines:
        match = re.match(r"\[(\d+-\d+-\d+ \d+:\d+)\] (\w+) ([\d#]+|\w+)", line)
        time = datetime.datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
        parsed_lines.append((time, match.group(2), match.group(3)))
        
    parsed_lines.sort()

    sleep_amount = [0]*10000

    i = 0
    while i < len(parsed_lines):
        guard_id = int(parsed_lines[i][2].strip('#'))
        while i+1 < len(parsed_lines) and parsed_lines[i+1][1] != "Guard":
            time_delta = parsed_lines[i+2][0] - parsed_lines[i+1][0]
            sleep_amount[guard_id] += time_delta.seconds // 60
            i += 2
        i += 1

    mx = max(sleep_amount)
    gidx = sleep_amount.index(mx)

    sleep_minutes = [0]*60
    i = 0
    while i < len(parsed_lines):
        guard_id = int(parsed_lines[i][2].strip('#'))
        while i+1 < len(parsed_lines) and parsed_lines[i+1][1] != "Guard":
            if guard_id == gidx:
                start = parsed_lines[i+1][0].minute
                end = parsed_lines[i+2][0].minute
                for j in range(start, end):
                    sleep_minutes[j] += 1
            i += 2
        i += 1

    mx = max(sleep_minutes)
    midx = sleep_minutes.index(mx)

    print("Strategy 1: {}".format(gidx*midx))

    sleep_minutes = [[0 for i in range(60)] for j in range(10000)]
    i = 0
    while i < len(parsed_lines):
        guard_id = int(parsed_lines[i][2].strip('#'))
        while i+1 < len(parsed_lines) and parsed_lines[i+1][1] != "Guard":
            start = parsed_lines[i+1][0].minute
            end = parsed_lines[i+2][0].minute
            for j in range(start, end):
                sleep_minutes[guard_id][j] += 1
            i += 2
        i += 1

    most_sleep = 0
    most_sleep_guard = 0
    most_sleep_minute = 0
    for g in range(len(sleep_minutes)):
        m = max(sleep_minutes[g])
        if m > most_sleep:
            most_sleep = m
            most_sleep_minute = sleep_minutes[g].index(m)
            most_sleep_guard = g

    print("Strategy 2: {}".format(most_sleep_minute*most_sleep_guard))

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
