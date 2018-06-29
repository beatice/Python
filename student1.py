#!/usr/bin/env python3
number = int(input("Please enter the number of students: "))
subjects = ('physics', 'math', 'history')
data = {}

for i in range(0, number):
    name = input("Please enter the name of student {}:".format(i+1))
    marks = []
    for x in subjects:
        marks.append(int(input("Enter the mark of {}(0 -100): ".format(x))))
    data[name] = marks

print("*" * 50)
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks: {}".format(x, total), end=' ')
    if total < 120:
        print("failed :(")
    else:
        print("passed :)")
