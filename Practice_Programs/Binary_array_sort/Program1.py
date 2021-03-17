def sortBinaryArray(a,n):
    j = -1
    for i in range(n):
        if a[i] < 1:
            j = j + 1
            a[i], a[j] = a[j], a[i]

arr = [1,1,0,0,0,1,1,1,0,1]
n = len(arr)
sortBinaryArray(arr,n)
for i in range(n):
    print(arr[i],end=" ")