from os import *
from sys import *
from collections import *
from math import *

def isPerfectSquare(n):
    if int(sqrt(n))*int(sqrt(n))==n:
        return 1
    else:
        return 0
# https://www.codingninjas.com/codestudio/problems/valid-perfect-square_1082552?leftPanelTab=1