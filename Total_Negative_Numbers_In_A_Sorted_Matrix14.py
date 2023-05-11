from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countNegativeNumbers(mat: List[List[int]]) -> int:
    # write nyour code here
    pass
    count=0
    for i in mat:
        for j in i:
            if j<0:
                count+=1
    return count
#https://www.codingninjas.com/codestudio/problems/total-negative-numbers-in-a-sorted-matrix_3161878