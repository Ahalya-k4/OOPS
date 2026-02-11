# Task 5: __call__ (Callable Object Task)
# Problem Statement:
# Create a class Calculator.
# Requirements:
# Attributes:
# no attributes required
# Implement:
# __call__(a, b) → return sum of a and b
# Task:
# Create object and call it like a function:
# obj = Calculator()
# print(obj(10, 20))

class Caluculator:
    def __call__(self,a,b):
        return a+b
    
obj= Caluculator()
print(obj(10,20))