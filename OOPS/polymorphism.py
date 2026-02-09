#polymorphism
#Task-1: Polymorphism – Payment System
#Problem Statement
#Create a program for a Payment System using method overriding.
#Requirements
#Create a parent class Payment
#method: pay()
#Create child class GooglePay (inherits Payment)
#override pay()
#Create child class PhonePe (inherits Payment)
#override pay()
#Create child class CreditCard (inherits Payment)
#override pay()
#Create one object for each class and call pay() method.

# Parent Class
class Payment:
    def pay(self):
        print("Processing a generic payment..")


class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay.")


class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe.")

class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card.")


p1 = Payment()
p2 = GooglePay()
p3 = PhonePe()
p4 = CreditCard()

p1.pay()   
p2.pay()   
p3.pay()   
p4.pay()   
