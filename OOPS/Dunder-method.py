# Dunder-double underscore method
# __init__,__repr__,__equal__,__enter__
# __new__,__len__,__str__,__add__,__exist__

class emp():
    def __init__(self,name,salary):
         self.name=name
         self.salary=salary

    #  def __str__(self):
    #      return f"employee name is {self.name} and {self.salary} is his salary"
    
    def __repr__(self):
         return f" {self.name}"
     
    def __len__(self):
        arr=[1,2,3,4,5]
        sum=0
        for i in arr:
           sum+=1
        return sum
    def __add__(self,other):
        return self.salary + other.salary
    
# e=emp("Abhi",5000)
# print(e)      

# print(len(e))

e1=emp("abhi",50000)
e2=emp("balu",10000)


print(e1+e2)