for t in range(int(input())):
    a=list(map(int,input().split('/')))
    b=list(map(int,input().split('/')))
    ans=0
    if b[1]>a[1]:
        ans-=1
    elif b[1]==a[1]:
        if b[0]>a[0]:
            ans-=1
    ans+=a[2]-b[2]
    print(ans)