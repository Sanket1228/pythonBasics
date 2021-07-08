from itertools import combinations_with_replacement

s, k = input().split()

s = sorted(list(s))
k = int(k)

l = combinations_with_replacement(s,k)
for j in l:
    print("".join(j))
