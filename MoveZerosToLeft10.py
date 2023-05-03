from os import *
from sys import *
from collections import *
from math import *
arr=list(map(int,input().split()))
n=len(arr)
def moveZerosToLeft(arr, n):
    result=list()
    countofzero=arr.count(0)
    for i in range(countofzero):
        result.append(0)
    for j in arr:
        if j!=0:
            result.append(j)
    for k in range(n):
        arr[k]=result[k]
    return arr
arr=moveZerosToLeft(arr,n)
print(arr)