#!/usr/bin/env python3
import sys

l = len(sys.argv)
for i in range(0,l):
    print(i, sys.argv[i])

try:
    if(int(sys.argv[1]) >= 0):
        hour = int(sys.argv[1]) // 60
        minutes = int(sys.argv[1]) % 60
        print("{} H, {} M".format(hour, minutes))
    else:
        raise ValueError
except ValueError:
    print("ValueError: Input number cannot be negative")
