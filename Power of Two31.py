from os import *
from sys import *
from collections import *
from math import *

def isPowerOfTwo(n):
    def rec(n):
        if n==1:
            return 1
        elif n%2!=0:
            return 0
        else:
            return rec(n//2) 
    return rec(n)
# https://www.codingninjas.com/codestudio/problems/power-of-two_893061?leftPanelTab=1