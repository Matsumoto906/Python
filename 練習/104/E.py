for t in range(int(input())):
    s=int(input())
    x=bin(s)[2:]
    ans=0
    for i in x:
        if i=='1':
            ans+=1
    print(ans)