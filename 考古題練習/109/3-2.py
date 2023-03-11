for i in range(0,int(input())):
    num=list(map(int,input().split()))
    tot=0
    ans=0
    for i in num:
        tot+=i
        if tot<0:
            tot=0
        if tot>ans:
            ans=tot
    if ans==0 and 0 not in num:
        ans=-65535
        for i in num:
            tot+=i
            if tot>ans and tot!=0:
                ans=tot
            if tot<0:
                tot=0
        print(ans)
    else:
        print(ans)