#!/usr/bin/env python3
s = input("Please enter a string: ")
l = len(s)
i = 0
j = -1
m = ''

while i < l and j > 0 - l:
    if s[i] == s[j]:
        i += 1
        j -= 1
        continue
    else:
        m = "wrong"
        break

if m == "wrong":
    print("The string is not t a palindrome")
else:
    print("The string is a palindrome")
