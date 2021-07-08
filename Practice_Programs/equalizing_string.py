if __name__ == '__main__':
        n = int(input())
        a = list(input())
        b = list(input())
        c = 0
        for i in range(0,n):
                if a[i] == b[i]:
                        pass
                else:
                        if a[i] == b[i+1] and a[i+1] == b[i]:
                                a[i], a[i+1] = a[i+1],a[i]
                                c += 1
                        else:
                                a[i] = b[i]
                                c += 1
        
        print(c)