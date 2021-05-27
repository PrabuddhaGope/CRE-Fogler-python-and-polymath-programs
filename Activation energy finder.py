# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:44:22 2021

@author: Prabuddha Gope
"""

#A simple program to calculate the activation energy of a reaction given the rate at two temperatures
import math

k1 = float(input("Enter k1 : "))
T1 = float(input("Enter T1(K) : "))
k2 = float(input("Enter k2 : "))
T2 = float(input("Enter T2(K) : "))

R = 10.73   #ft^3 - psi / Rankine - lb-mol

E = math.log(k1/k2) * R / (1/T2 - 1/T1)
print(E)
