#!/usr/bin/env python3
'''
#def greet_programmer():
   # pass
def greet_programmer():
    print("Hello, programmer!")


#def greet(name):
   # pass
   def greet(name):
    print(f"Hello, {name}!")


#def greet_with_default(name="programmer"):
    #pass
    def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


#def add(num1, num2):
    #pass
    def add(num1, num2):
    return num1 + num2

#def halve(number):
   # pass
   def halve(number):
    if isinstance(number, (int, float)):
        return number / 2


'''
def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if isinstance(number, (int, float)):
        return number / 2
