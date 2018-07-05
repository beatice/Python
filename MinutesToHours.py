#!/usr/bin/env python3
import sys

def Hour(m):
    hour = int(m) // 60
    minutes = int(m) % 60
    print("{} H, {} M".format(hour, minutes))
        
try:
    if(int(sys.argv[1]) >= 0):
        Hour(sys.argv[1])
    else:
        raise ValueError
except ValueError:
    print("ValueError: Input number cannot be negative")
