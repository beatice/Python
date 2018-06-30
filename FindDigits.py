#!/usr/bin/env python3
s = input("Please enter a string:" )
l = len(s)
digits = []

for i in range(0:l):
    if s[i].isdigit():
        digits.append(s[i])
    else:
        continue
        
print("".join(digits))
