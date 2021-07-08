import numpy as np
for _ in range(int(input())):
    n,m = input().split()
    mat = []
    result = []
    for i in range(int(n)):
        mat.append(list(map(int,input().split())))

    mx = np.amax(mat)
    mi = np.amin(mat)
    
    for i , e in enumerate(mat):
        for j, ee in enumerate(e):
            if ee == mx:
                mat = np.delete(mat,i,0)
                mat = np.delete(mat,j,1)
            if ee == mi:
                # mat = np.delete(mat,i,0)
                mat = np.delete(mat,j,1)

    # print(mx1)
    # print(mx2)
    # print(mi1)
    # print(mi2)
    print(mat)            