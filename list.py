#!/usr/bin/env python3
a = [1, 34, 33.5, 543, 'ouuu', "plo"]
print("List Examples")
print()
print("a[:]  ", a[:])

#读取列表中数据
print("-" * 50)
i = 0
while i < len(a):
    print("a[{}]: {}".format(i, a[i]))
    i += 1

print("-" * 50)
i = 0
j = -1
while i < len(a):
    print("a[{}]: {}".format(j, a[j]))
    i += 1
    j -= 1

print("-" * 50)
i = 0
while i < len(a):
    print("a[{}:] {}".format(i, a[i:]))
    i += 1

print("-" * 50)
i = 1
while i <= len(a):
    print("a[:{}] {}".format(i, a[:i]))
    i += 1

print("-" * 50)
i = 0
j = -1
while i < len(a):
    print("a[:{}] {}".format(j, a[:j]))
    i += 1
    j -= 1

print("-" * 50)
i = 0
j = -1
while i < len(a):
    print("a[{}:] {}".format(j, a[j:]))
    i += 1
    j -= 1

