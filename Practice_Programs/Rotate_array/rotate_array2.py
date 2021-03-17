def rotateArray(arr,d,n):
    arr[0:d] = reversed(arr[0:d])
    arr[d:n] = reversed(arr[d:n])
    arr[0:n] = reversed(arr[0:n])

def printArray(arr,n):
    for i in range(n):
        print(arr[i],end=" ")

arr = [1,2,3,4,5,6,7]
rotateArray(arr,2,7)
printArray(arr,7)