# Task 9: __gt__, __lt__ (Comparison Task)
# Problem Statement:
# Create a class Employee.
# Requirements:
# Attributes:
# name
# salary
# Implement:
# __gt__() → compare based on salary
# __lt__() → compare based on salary
# Task:
# Compare employees using:
# e1 > e2
# e1 < e2


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __gt__(self,other):
        if isinstance(other,Employee):
            return self.salary>other.salary
        return NotImplemented

    def __lt__(self,other):
        if isinstance(other,Employee):
            return self.salary<other.salary
        return NotImplemented
    
e1=Employee("bob",5000)
e2=Employee("abhi",6000)

print(e1>e2)
print(e1<e2)