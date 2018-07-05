#!/usr/bin/env python3
import sys

l = len(sys.argv)
for i in range(0,l):
    print(sys.argv[i])

try:
    if(sys.argv[1] < 0):
        raise ValueError
    else:
        hour = sys.argv[1] / 60
        minutes = mod(sys.argv[1], 60)
except:
    print("ValueError: Input number cannot be negative")
