def sortBinaryArray(arr,n):
    zero = arr.count(0)
    ones = arr.count(1)
    final = []
    for i in range(zero):
        final.append(0)
    for i in range(ones):
        final.append(1)
    return final

arr = [1,1,0,0,0,1,1,1,0,1]
n = len(arr)
res = sortBinaryArray(arr,n)
for i in range(n):
    print(res[i],end=" ")