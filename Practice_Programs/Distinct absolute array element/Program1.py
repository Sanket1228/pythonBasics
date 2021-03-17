def findDistinct(arr):
    s = set([abs(i) for i in arr])
    return len(s)

arr = [-3 ,-2 ,0 ,3 ,4 ,5]
print(findDistinct(arr))