def count_number(num):
    counter = 0
    while num != 0:
        num = num//10 
        counter += 1
        
    return counter        

def searchA(Arr, x):
    indices = []
    for i in range(len(Arr)):
        if Arr[i] == x:
            indices.append(i)
    
    return indices

def Minimum(Arr, starting, ending):
    Minimum = 1000000
    index = 0
    for i in range(starting, ending):
        if Arr[i] < Minimum:
             Minimum = Arr[i]
             index = i
    
    return index
        
def Sort4(Arr):
    for i in range(len(Arr)):
        smallest_index = Minimum(Arr, i, len(Arr))    
        temp = Arr[smallest_index]
        Arr[smallest_index] = Arr[i]
        Arr[i] = temp

def reverseString(string, starting, ending):
    return string[ending: starting: -1]

def IterativeSum(num):
    sum = 0
    while num != 0:
        n = num%10
        num = num//10
        sum += n
    return sum

def RecursiveSum(num):
    if count_number(num) == 1:
        return num
    else:
        return (num%10) + RecursiveSum(num//10)

def sortedMerge(Arr1, Arr2):
    i = 0
    j = 0
    k = 0
    A = [0]*(len(Arr1)+len(Arr2))
    while i < len(Arr1) and j < len(Arr2):
        if Arr1[i] < Arr2[j]:
            A[k] = Arr1[i]
            i += 1
        else:
            A[k] = Arr2[j]
            j += 1
        k += 1
    
    while i < len(Arr1):
        A[k] = Arr1[i]
        i += 1
        k += 1
    
    while j < len(Arr2):
        A[k] = Arr2[j]
        j += 1
        k += 1
    return A

def isPolindrome(string):
    if len(string) == 1:
        return string
    else:
        return str(isPolindrome(string[1:])) + string[0]
    
def Sort10(Arr):
    P = []
    N = []
    for i in range(len(Arr)):
        if Arr[i] < 0:
            N.append(Arr[i])
        else:
            P.append(Arr[i])
    
    Sort4(P)
    Sort4(N)
    
    i = 0
    j = 0
    k = 0
    
    while i < len(P) and j < len(N):
        Arr[k] = N[i]
        Arr[k+1] = P[j]
        i += 1
        j += 1
        k += 2
    
    while i < len(P):
        Arr[k] = P[i]
        i += 1
        k += 1
    
    while j < len(N):
        Arr[k] = N[j]
        j += 1
        k += 1
    
    

Arr = [22,2,1,7,11,13,5,2,9]

print(searchA(Arr, 2))
print(Minimum(Arr, 3, 8))
Sort4(Arr)
print(Arr)

S = "University of Engineering and Technology Lahore"

print(reverseString(S, 26, 39))
print(IterativeSum(1524))
print(RecursiveSum(1524))

Arr1 = [1,2,3,9,11,15]
Arr2 = [4,6,7,8]

print(sortedMerge(Arr1, Arr2))

string = "radar"

print(string == isPolindrome(string))

a = [10, -1, 9, 20, -3, -8, 22, 9, 7]

Sort10(a)

print(a)