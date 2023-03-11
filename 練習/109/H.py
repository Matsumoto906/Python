def f(l,u,k):
    for i in l:
        if i[0] not in u and i[0]==k:
            u.append(i[0])
            k=i[1]
            break
    if k in u:
        return len(u)
    else:
        return f(l,u,k)

for tt in range(int(input())):
    num=[]
    use=[]
    g=[]
    k=0
    for t in range(int(input())):
        s=list(map(int,input().split()))
        if s[0] not in g:
            g.append(s[0])
        if s[1] not in g:
            g.append(s[1])
        num.append(s)
    g.sort()
    for i in g:
        use.clear()
        if f(num,use,i) > k:
            k=f(num,use,i)
            ans=i
    print(ans)