import itertools

if __name__ == '__main__':
    s = input()
    even = set()
    for i in range(len(s)):
        if s[i].isdigit():
            even.add(s[i])

            li = list(itertools.permutations(s,len(s)))

    print(li)
        
