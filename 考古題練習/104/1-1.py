for t in range(int(input())):
    input()
    s=list(map(int,input().split(',')))
    ans=0
    for i in range(0,len(s)-1):
        if s[i]<s[i+1]:
            ans+=(s[i+1]-s[i])*20
        else:
            ans+=(s[i]-s[i+1])*10
    print(ans)