for t in range(int(input())):
    s=list(map(str,input().split()))
    ans=0
    for i in s:
        if 's' in i or 'S' in i:
            ans+=1
    print(len(s),ans)