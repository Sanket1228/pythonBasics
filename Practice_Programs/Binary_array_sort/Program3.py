def sortBinaryArray(arr,n):
    arr.sort()
    return arr

arr = [1,1,0,0,0,1,1,1,0,1]
n = len(arr)
sortBinaryArray(arr,n)
for i in range(n):
    print(arr[i],end=" ")