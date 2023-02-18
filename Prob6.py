# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:36:57 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    number = int(input("Enter digits: "))
    print("sum of digits is: ", funcs.SumIterative(number))
    print("sum of digits is: ", funcs.SumRecursive(number))
    
if __name__ == "__main__":
    main()