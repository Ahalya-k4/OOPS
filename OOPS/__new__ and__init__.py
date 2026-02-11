# Task 3: __new__ and __init__ (Object Creation Flow Task)
# Problem Statement:
# Create a class User.
# Requirements:
# Attributes:
# name
# Implement:
# __new__() → print "Object is being created"
# __init__() → print "Object is initialized"
# Task:
# Create an object and observe constructor execution order.


class User:
    def __new__(cls,*args,**kwargs):
        print("Object is being created")
        return super().__new__(cls)

    def __init__(self,name):
        print("Object is initialized")
        self.name=name

u=User("alice")


