class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def __eq__(self,other):
        if isinstance(other,Mobile):
            return self.brand == other.brand
        return False
    
m1=Mobile("samsung","s21",70000)
m2=Mobile("Aplle","iphone 14",80000)

print(m1==m2)