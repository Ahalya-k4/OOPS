# Task 2 (Class Variable + Classmethod + Staticmethod) – Simple Problem Statement
# Problem: Student College System
# You want to create a student system where college name is same for all students.
# What to do
# Create class Student with:
# Class Variable
# college_name = "ABC College"
#  (common for all students)
# Constructor
# takes name and roll_no
# Classmethod
# change_college(new_name)
#  to update the college name for all students.
# Staticmethod
# is_pass(marks)
#  returns pass or fail (example: pass if marks >= 35)
# Instance method
# display() prints student details
# How it works
# Create 2 students
# Print both details
# Change college using classmethod
# Print again → both students should show new college name
# Use staticmethod to check pass/fail
# Main point
# Class variable = shared memory
# Classmethod = updates shared data
# Staticmethod = helper function (not depending on object)

class Student:

    college_name = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks>=35:
            print("pass")
        else:
            print("fail")

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("\n")


s1 = Student("Rahul", 101)
s2 = Student("Anita", 102)

print("Before changing college name")
s1.display()
s2.display()

Student.change_college("XYZ College")

print("After changing college name")
s1.display()
s2.display()

Student.is_pass(78)
Student.is_pass(30)

