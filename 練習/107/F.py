for t in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    ans=0
    for g in range(e,f+1):
        for i in range(a,b+1):
            for j in range(c,d+1):
                if (i+j)%g==(i-j)%g:
                    ans+=1
    print(ans)