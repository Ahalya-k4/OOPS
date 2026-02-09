# Abstraction –

#syntax:
#from abc from ABC,abstractmethod
#class A(ABC):
#@abstractmethod
# def abs_method(self):
#pass
#concrete method
# def concrete_method(self):
#implementation
#class B(A):
# def abs_method(self):
#implementation

#example:
#  Vehicle System
#Problem Statement
#Create a program for a Vehicle System using Abstraction.
#Requirements
#Create an abstract class Vehicle
#abstract method: start_engine()
#Create child class Car
#implement start_engine()
#Create child class Bike
#implement start_engine()
#Create child class Bus
#implement start_engine()
#Create objects and call start_engine() method.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
   


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")


class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")


class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started.")


v1 = Car()
v2 = Bike()
v3 = Bus()

v1.start_engine()
v2.start_engine()
v3.start_engine()

