# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:36:57 2022

@author: USER
"""

from funcs import funcs

# Defining Main Function
def main():
    A = [[1,13,13],[5,11,6],[4,4,9]]
    columnSum = funcs.ColumnWiseSum(A)
    print(A)
    print("")
    print(columnSum[0])
    print(columnSum[1])
    print(columnSum[2])
    rowSum = funcs.RowWiseSum(A)
    print("")
    print(rowSum[0], rowSum[1], rowSum[2])
       
if __name__ == "__main__":
    main()