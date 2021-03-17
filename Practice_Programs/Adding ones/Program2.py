n,k = map(int,input().split())
x = [0] * n
arr = list(map(int,input().split()))
for i in arr:
    for j in range(i-1,n):
        x[j] += 1

for i in x:
    print(i,end=" ")        