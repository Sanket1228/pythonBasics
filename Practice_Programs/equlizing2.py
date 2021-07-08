n = int(input())
a = list(input())
b = list(input())

count = 0
for i in range(0,n):
    if a[i] == b[i]:
        pass
    else:
        a[i] = b[i]
        count += 1

print(count)
