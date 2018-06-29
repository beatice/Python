#!/usr/bin/env python3
# Star1
x = int(input("Enter the number of stars: "))
while x >= 1:
    print("*" * x)
    x -= 1

#Star2
x = int(input("Enter the number of stars: "))
n = 1
while n <= x:
    print("*" * n)
    n += 1

#Star3
x = int(input("Enter the number of stars: "))
n = 0
y = x
while n <= x:
    print(" " * n, end='')
    print("*" * y)
    n += 1
    y -= 1

   
