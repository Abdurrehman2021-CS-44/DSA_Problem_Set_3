# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 21:12:30 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    num1 = int(input("How many element you want to take in Array A: "))
    Arr1 = funcs.TakingArrayAsInput(num1)
    num2 = int(input("How many element you want to take in Array B: "))
    Arr2 = funcs.TakingArrayAsInput(num2) 
    print("A = " , Arr1)
    print("B = " , Arr2)
    print(funcs.SortedMerge(Arr1, Arr2))
       
if __name__ == "__main__":
    main()
