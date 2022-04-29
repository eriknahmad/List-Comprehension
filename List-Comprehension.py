#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Project Name: List Comprehension
# File Name: List-Comprehension.py
# Author: Erik Nahmad
# Date: May 1 2021
# Purpose: To demonstrate five permutations of code that return the squares of a list of numbers


list = [1,2,3,4,5,6,7,8,9]
squares = []
for x in list:
  squares.append(x*x)
print(squares)


squares = []
for x in range(1, 10):
  squares.append(x*x)
print(squares)


squares = []
for x in range(1, 10): squares.append(x*x)
print(squares)


squares = [x*x for x in range(1, 10)]
print(squares)


print(squares := [x*x for x in range(1, 10)])
