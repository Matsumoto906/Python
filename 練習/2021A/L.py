for t in range(int(input())):
    input()
    s=list(map(int,input().split()))
    num=[]
    num.append(s)
    for i in range(int(input())):
        s=list(map(int,input().split()))
        num.append(s)
    x1=0
    y1=20
    for i in num:
        i=i[0]
        if i>x1:
            x1=i
        if i<y1:
            y1=i
    x2=0
    y2=20
    for i in num:
        i=i[1]
        if i>x2:
            x2=i
        if i<y2:
            y2=i
    ans=(x1-y1+x2-y2)*2
    print('The shortest path has length',ans)