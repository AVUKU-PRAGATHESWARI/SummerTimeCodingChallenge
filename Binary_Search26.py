def search(nums: [int], target: int):
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid 
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1
# https://www.codingninjas.com/codestudio/problems/binary-search_972?leftPanelTab=0
