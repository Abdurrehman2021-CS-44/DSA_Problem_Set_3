# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 17:42:58 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    path = "ArrayNumbers.txt"
    X = funcs().readDataFromFileP1(path)
    Arr = funcs.Sort4(X)
    print(Arr)
    x = int(input("Enter the number: "))
    print(funcs.SearchB(Arr, x))
    
if __name__ == "__main__":
    main()