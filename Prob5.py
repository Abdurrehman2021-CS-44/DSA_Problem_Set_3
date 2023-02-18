# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:06:21 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    path = "String.txt"
    s = funcs.readDataFromFileP5(path)
    print(s)
    start = int(input("Starting Index: "))
    end = int(input("Ending Index: "))
    print(funcs.StringReverse(s, end, start))
    
if __name__ == "__main__":
    main()