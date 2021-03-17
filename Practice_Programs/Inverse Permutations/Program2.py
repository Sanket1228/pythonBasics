def inversePermutation(arr,size):
    arr2 = [0] * size
    for i in range(0,size):
        arr2[arr[i]-1] = i + 1
    for i in range(0,size):
        print(arr2[i],end=" ")

arr = [2,3,4,5,1]
size = len(arr)
inversePermutation(arr,size)