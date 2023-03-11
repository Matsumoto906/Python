for t in range(int(input())):
    num=list(map(int,input().split()))
    ans=-9999999999999
    k=0
    for i in num:
        k+=i
        if k>ans:
            ans=k
        if k<0:
            k=0
    print(ans)