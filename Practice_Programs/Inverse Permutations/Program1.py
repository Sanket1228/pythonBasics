def inversePermutation(arr,size):
    for i in range(0,size):
        for j in range(0,size):
            if arr[j] == i+1:
                print(j+1,end=" ")
                break

arr = [2,3,4,5,1]
size = len(arr)
inversePermutation(arr,size)