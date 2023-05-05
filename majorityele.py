from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	dict1={}
	for i in range(n):
		if arr[i] not in dict1.keys():
			dict1[arr[i]]=0
		else:
			dict1[arr[i]]+=1
	ans=list(dict1.keys())
	check=list(dict1.values())
	if max(check)>=floor(n/2):
		return ans[check.index(max(check))]
	else:
		return -1