#!/usr/bin/env python3
number = int(input("Please enter the number of students: "))
subjects = ('physics', 'math', 'history')
data = []

for i in range(0, number):
    name = input("Please enter the name of student {}:".format(i+1))
    student = []
    student.append(name)
    mark = []
    for x in subjects:
        mark.append(int(input("Please enter {}'s {} grade(0-100): ".format(name, x))))
    student.append(mark)
    data.append(student)

print("*" * 50)
for i in range(0, number):
    print("Student {}: {:10s}, Total grade: {:6d} ".format(i+1, data[i][0], sum(data[i][1])), end=' ')
    if sum(data[i][1]) < 120:
        print("failed")
    else:
        print("passed")
