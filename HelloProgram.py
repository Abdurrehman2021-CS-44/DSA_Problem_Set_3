# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random 
array  = []

min = 0
max = 20

n = 5

for i in range(0,n):
    num = random.randint(min, max)
    array.append(num)
    
for i in range(0,n):
    print(array[i])