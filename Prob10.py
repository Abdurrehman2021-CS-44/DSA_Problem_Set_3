# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:07:10 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    path = "NumbersForProb10.txt"
    X = funcs().readDataFromFileP1(path)
    print("Input: " , X)
    print("Output" , funcs.Sort10(X))
       
if __name__ == "__main__":
    main()