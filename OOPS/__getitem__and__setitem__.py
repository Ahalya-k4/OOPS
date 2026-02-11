# Task 6: __getitem__ and __setitem__ (Indexing Task)
# Problem Statement:
# Create a class ShoppingCart.
# Requirements:
# Store items in list internally.
# Implement:
# __getitem__(index) → return item at index
# __setitem__(index, value) → update item at index
# Task:
# Create object with items and update using:
# cart[0]
# cart[1] = "New Item"


class ShoppingCart:
    def __init__(self,items):
        self.items=items

    def __getitem__(self,index):
        return self.items[index]
    
    def __setitem__(self,index,value):
        self.items[index]=value

cart=ShoppingCart(["shirt","shoes","watch"])        

print(cart[0])
cart[1]="new Item"
print(cart.items)