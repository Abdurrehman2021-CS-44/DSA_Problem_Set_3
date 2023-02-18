# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:44:05 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    num = int(input("How many element you want to take in array: "))
    Arr = funcs.TakingArrayAsInput(num)
    print(funcs.Sort4(Arr))
    
if __name__ == "__main__":
    main()