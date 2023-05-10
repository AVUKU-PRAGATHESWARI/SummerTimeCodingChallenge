from os import *
from sys import *
from collections import *
from math import *

import sys

def reverseString(string):
    return string[::-1]
    pass

t = int(sys.stdin.readline().strip())

for i in range(t):
    
    string = str(sys.stdin.readline().strip())
    
    for i in (reverseString(string)):
        print(i, end = '')
        
    print()
#https://www.codingninjas.com/codestudio/problems/reverse-the-string_799927?leftPanelTab=1