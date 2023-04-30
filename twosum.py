def twoSum(arr, target, n):
    d={}
    ans=[]
    for i in range(n):
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
        if target-arr[i] not in d:
            continue
        if target-arr[i] == arr[i]:
            if d[target-arr[i]]>1:
                ans.append([arr[i], target-arr[i]])
                d[target-arr[i]]-=2
        else:
                if d[target-arr[i]]>0 and d[arr[i]]>0:
                    ans.append([arr[i], target-arr[i]])
                    d[target-arr[i]]-=1
                    d[arr[i]]-=1
    if len(ans)==0:
        return [[-1, -1]]
    return ans
    pass

def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)