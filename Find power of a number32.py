from os import *
from sys import *
from collections import *
from math import *

def pow(X, N):
    def power(X,N):
        if N==0:
            return 1  
        else:
            return X*power(X,N-1)
    return power(X,N)