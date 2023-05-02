arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=arr1+arr2 
arr3.sort()
arr3=[ele for ele in arr3 if ele!=0]
print(arr3)
