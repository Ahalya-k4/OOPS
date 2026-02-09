class A:
    __x=11
    def __init__(self):
        pass
    @classmethod
    def incrementation(cls):
        cls.x+=1

    def display_sum(a,b):
        print(a+b)

class B(A):
    def inc(self):
        self.x+=1
        print(self.x)

class C(A):
    def inc(self):
        self.x+=1
        print(self.x)

#a=A()
#a.x+=1 #11
#A.x+=1 # all output is 11
#a.incrementation()
#print(a.x)
A.display_sum(1,2)

#b=B()
#b.inc()
#print(b.x)

#c=C()
#print(c.x)