from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def conc(self):
        print("i am concrete method")

class B(A):
    def method1(self):
        print("i am in class B")
    def method2(self):
        print("method-2")
    
obj=B()
#obj.method1()
obj.conc()