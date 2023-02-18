# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:02:23 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    num = int(input("How many element you want to take in array: "))
    Arr = funcs.TakingArrayAsInput(num)
    starting = int(input("Enter Starting Index: "))
    ending = int(input("Enter Ending Index: "))
    print (funcs.Minimum(Arr, starting, ending+1))
    
if __name__ == "__main__":
    main()