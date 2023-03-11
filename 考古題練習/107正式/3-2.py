for t in range(int(input())):
    a1,a2,b1,b2,c1,c2=(map(int,input().split()))
    a=[]
    b=[]
    c=[]
    con=0
    for i in range(a1,a2+1):
        a.append(i)
    for i in range(b1,b2+1):
        b.append(i)
    for i in range(c1,c2+1):
        c.append(i)
    for i in a:
        for j in b:
            for k in c:
                if (i+j)%k==(i-j)%k:
                    con+=1
    print(con)