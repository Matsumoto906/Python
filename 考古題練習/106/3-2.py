for t in range(int(input())):
    s=list(map(int,input().split(', ')))
    a=s.copy()
    a.sort()
    for i in a:
        if i!=a[-1]:
            print(s.index(i)+1,end=', ')
        else:
            print(s.index(i)+1)