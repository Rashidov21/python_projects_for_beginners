# -*- coding: utf-8 -*-
import math

# print(math.factorial(10))


# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#     	r = n*factorial_recursive(n-1)
#     return r

# print(factorial_recursive(5))

# class Parent:
#   def __init__(self, color):
#     self.color =  color
#
#   def print_color(self):
#     print(self.color)
#
# class Child(Parent):
#   def __init__(self, color, name):
#     super().__init__(color)
#
#
#
# x = Child('Negr')
#
# x.print_color()

m = input()
n = m.split(" ")
n.reverse()
print("".join(n))

