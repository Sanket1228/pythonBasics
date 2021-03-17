arr = [-3 ,-2 ,0 ,3 ,4 ,5]
b = []
n1 = 0
count = 0    
for i in arr:
    n1 = abs(i)
    if n1 not in b:
        b.append(n1)
        count += 1
    
print(count)
