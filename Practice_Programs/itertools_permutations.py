from itertools import permutations
s, k = input().split()

s = sorted(list(s))
k = int(k)
l = permutations(s,k)
for i in l:
    print("".join(i))

