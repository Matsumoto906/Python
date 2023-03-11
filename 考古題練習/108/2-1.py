for t in range(int(input())):
    a,b,c=map(int,input().split())
    ans=[]
    for i in range(a,b+1):
        if str(c) in str(i):
            ans.append(i)
    print(len(ans))
    