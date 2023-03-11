ans=[]
for t in range(int(input())):
    s=list(map(int,input().split(',')))
    s.sort()
    m=min(s)
    n=1
    for j in range(1,m+1):
        key=True
        for i in s:
            if i%j!=0:
                key=False
                break
        if key==True:
            n=j
    ans.append(n)
for i in ans:
    print(i)
