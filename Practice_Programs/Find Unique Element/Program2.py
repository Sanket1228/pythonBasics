a = [6,2,5,2,2,6,6]
n,k = 7,3
count = {}
for i in range(n):
    count[a[i]] = count.get(a[i],0)+1
for key,value in count.items():
    if value == 1:
        print(key)
        break