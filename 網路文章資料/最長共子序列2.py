for i in range(int(input())):
    x=input().strip()
    y=input().strip()
    d=[[0 for i in range(0,len(x)+1)] for j in range(0,len(y)+1)]

    for a in range(0,len(y)):
        for b in range(0,len(x)):
            if y[a]==x[b] :
                d[a+1][b+1]=d[a][b]+1
            else:
                d[a+1][b+1]=max(d[a+1][b],d[a][b+1])
    print(d[a+1][b+1])