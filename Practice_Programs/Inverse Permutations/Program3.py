def inversePermutation(arr,size):
    arr2 = sorted(arr)
    for i in range(size):
        for j in range(size):
            if arr2[i] == arr[j]:
                print(j+1,end=" ")
                break

arr = [2,3,4,5,1]
size = len(arr)
inversePermutation(arr,size)