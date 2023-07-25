# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 23:32:42 2023

@author: Hi
"""

#Dunder Methods(Magic Methods with double underscores __)

class Person:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self):
        return self.x + self.y
        
    def __repr__(self):
        return f"X: {self.x}"
    
P1 = Person(10, 11)
print(P1.__add__())