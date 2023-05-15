def findPeakElement(arr: [int]) -> int:
    for i in range(1,len(arr)-1):
        if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
            return arr[i]
# https://www.codingninjas.com/codestudio/problems/find-peak-element_1081482?leftPanelTab=1