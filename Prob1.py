# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 23:23:42 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    path = "ArrayNumbers.txt"
    X = funcs().readDataFromFileP1(path)
    print(X)
    x = int(input("Enter the number: "))
    print(funcs.SearchA(X, x))
    
if __name__ == "__main__":
    main()