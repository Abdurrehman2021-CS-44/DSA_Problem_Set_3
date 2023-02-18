# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:21:18 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    word = str(input("Word: "))
    if (funcs.PolindromeRecursive(word)):
        print("Polindrome")
    else:
        print("Not Polindrome")
       
if __name__ == "__main__":
    main()