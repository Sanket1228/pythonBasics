def rotateArray(arr,d,n):
    temp = arr[d:] + arr[:d]
    for i in range(n):
        print(temp[i],end=" ")

arr = [1,2,3,4,5,6,7]
rotateArray(arr,2,7)
