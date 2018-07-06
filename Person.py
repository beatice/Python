#!/usr/bin/env python3
import os
from collections import Counter

class Person(object):
    """ 返回具有给定名称的 Person 对象 """
    
    def __init__(self, name):
        self.name = name
    
    def get_details(self):
        return self.name
    
    def get_grade(self, grade):
        return self.grade

class Student(Person):
    """ 返回 Student 对象，采用 name, branch, year 3个参数 """
    
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
    
    def get_details(self):
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
    
    def get_grade(self, grade):
        c = Counter(grade)
        print("A: {}, 

class Teacher(Person):
    """ 返回 Teacher 对象，采用字符串列表作为参数 """
    
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers
        
    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))
    
    def get_grade(self, grade):
        
      
person1 = Person('Sam')
student1 = Student('Amy', 'CSE', 2009)
teacher1 = Teacher('John', ['Art', 'Computer', 'Management'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
