k = [int(i) for i in input().split()][0]
a = sorted([int(i) for i in input().split()])
b = [0]*(k+1)
lastb = len(b)
while len(a) > 0:
    i = a.pop()
    if lastb != i:
        for j in range(i,lastb):
            b[j] = len(a) + 1
            lastb = i
        
for i in b[1:]:
    print(i,end=" ")
