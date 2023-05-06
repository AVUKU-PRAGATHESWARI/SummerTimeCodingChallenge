def findDuplicate(arr):
    # Write your code here
    for i in arr:
        if arr.count(i)>1:
            return i
