#!/usr/bin/python3

# create a class student that has the attribute name, id, age, email
# - the age, email should be a private instance
# - create a method that would return the value of the email and the age of the student
# - create a method that prints out the following courses -> Biology, Physics, Computer Science


class Student:
    def __init__(self, name, ids, age, email):
        self.name = name
        self.ids = ids
        self.__age = age
        self.__email = email

    def record(self):
        print(f"{self.__age}, {self.__email}")

student1 = Student("Jesse", 123, 21, "ogujesse2@gmail.com")
student1.record()
