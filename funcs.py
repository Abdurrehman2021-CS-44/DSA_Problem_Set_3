# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 23:23:06 2022

@author: USER
"""

import os.path

class funcs:
    @staticmethod
    def SearchA(Arr, x):
        found = [0]*10
        j = 0
        for i in range(0, len(Arr), 1):
            if (Arr[i] == x):
                found[j] = int(i)
                j += 1
        return found
    
    @staticmethod
    def SearchB(Arr, x):
        found = [0]*10
        j = 0
        for i in range(0, len(Arr), 1):
            if (Arr[i] == x):
                found[j] = int(i)
                j += 1
        return found
    
    @staticmethod
    def Minimum(Arr, starting, ending):
        smallest = 10000
        idx = 0
        for i in range(starting, ending, 1):
            if(smallest > Arr[i]):
                smallest = Arr[i]
                idx = i;
        return idx;
    @staticmethod
    def TakingArrayAsInput(arrElements):
        arr = [0]*int(arrElements)
        print("Enter array as input: ")
        for i in range(0, int(arrElements), 1):
            arr[i] = int(input())
        return arr
    @staticmethod
    def Sort4(Arr):
        for i in range (0, len(Arr), 1):
            smallest_idx = funcs.Minimum(Arr, i, len(Arr));
            temp1 = Arr[smallest_idx];
            Arr[smallest_idx] = Arr[i];
            Arr[i] = temp1;
        return Arr
   
    @staticmethod
    def StringReverse(string, starting, ending):
       return (string[ starting: ending: -1])
        
    @staticmethod
    def SumIterative(number):
        count = funcs.countNumber(number)
        sum = 0
        for i in range(0, count, 1):
            num1 = int(number % 10)
            number = int(number / 10)
            sum += num1 
        return sum
    
    @staticmethod
    def SumRecursive(number):
        if (number == 0):
            return 0
        return int(number % 10 + funcs.SumRecursive(number / 10))
    
    @staticmethod
    def countNumber(number):
        i = number
        count = 0
        #for i in range (i,  i == 0, i = i/10):
        while (i != 0):
            i = int(i / 10)
            count += 1
        return count
    
    @staticmethod
    def ColumnWiseSum(Mat):
        columnSum = []
        for i in range(0, 3, 1):
            sum = 0
            for j in range(0, 3, 1):
                sum += Mat[i][j]
            columnSum.append(sum)
        return columnSum
        
    @staticmethod
    def RowWiseSum(Mat):
        rowSum = []
        for i in range(0, 3, 1):
            sum = 0
            for j in range(0, 3, 1):
                sum += Mat[j][i]
            rowSum.append(sum)
        return rowSum
        
    @staticmethod
    def SortedMerge(Arr1, Arr2):
        for i in range(0, len(Arr2), 1):
            Arr1.append(Arr2[i])
        for i in range (0, len(Arr1), 1):
            smallest_idx = funcs.Minimum(Arr1, i, len(Arr1));
            temp1 = Arr1[smallest_idx];
            Arr1[smallest_idx] = Arr1[i];
            Arr1[i] = temp1;
        return Arr1
        
    @staticmethod
    def isPolindromeRecursive(string):
        if (len(string) == 1):
            return string
        else:
            s1 = funcs.isPolindromeRecursive(string[1: ]) + string[0]
            return s1
    
    @staticmethod
    def PolindromeRecursive(string):
        if (string == funcs.isPolindromeRecursive(string)):
            return True
        else:
            return False
    
    @staticmethod
    def Sort10(Arr):
        A = []
        B = []
        for i in range(0, len(Arr), 1):
            if(Arr[i] >= 0):
                A.append(Arr[i])
            else:
                B.append(Arr[i])
        C = funcs.Sort4(A)
        D = funcs.Sort4(B)
        E = []
        j = 0
        count = 0
        if (len(C) > len(D)):
            for i in range(0, len(C), 1):
                if (count == 1 and i == j):
                    E.append(C[i])
                    j += 1
                    continue
                for j in range(j, len(D), 1):
                    if (C[j] < D[j]):
                        E.append(C[j])
                        E.append(D[j])
                    else:
                        E.append(D[j])
                        E.append(C[j])
                    j += 1 
                    if (j == len(D)):
                        count += 1
                        break
        if (len(C) < len(D)):
            for i in range(0, len(D), 1):
                if (count == 1 and i == j):
                    E.append(C[i])
                    j += 1
                    continue
                for j in range(j, len(C), 1):
                    if (C[j] < D[j]):
                        E.append(C[j])
                        E.append(D[j]) 
                    else:
                        E.append(D[j])
                        E.append(C[j])
                    j += 1
                    if (j == len(D)):
                        count += 1
                        break
        return E
    
    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2]
    
    @staticmethod
    def readDataFromFileP1(path):
        if (os.path.exists(path)):
            fileVariable = open(path, 'r')
            lines = fileVariable.read()
            numbers = []
            arr = lines.split()
            fileVariable.close()
            for n in arr:
                num = int(n)
                numbers.append(num)
            return numbers
        else:
            return None

    @staticmethod
    def readDataFromFileP5(path):
        if (os.path.exists(path)):
            fileVariable = open(path, 'r')
            records = fileVariable.read().split("\n")
            fileVariable.close()
            for line in records:
                string = line
                return string
        else:
            return None