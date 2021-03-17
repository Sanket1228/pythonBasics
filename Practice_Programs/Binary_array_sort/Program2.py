def sortBinaryArray(arr,n):
    cnt0 = 0

    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1
        
    i = 0
    while i < cnt0:
        arr[i] = 0
        i += 1

    while i < n:
        arr[i] = 1
        i += 1

    return arr

if __name__ == "__main__":
    n = int(input("Enter the number of inputs you want : "))
    arr = list(map(int, input("Enter the elements : ").split()))
    res = sortBinaryArray(arr,n)
    for i in range(n):
        print(res[i],end=" ")