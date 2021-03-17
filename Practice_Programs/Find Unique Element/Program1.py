arr = [6,2,5,2,2,6,6]
n,k = 7,3
m = 0
for i in range(n):
    m = (arr.count(arr[i]))
    if m == k:
        continue
    else:
        print(arr[i])   