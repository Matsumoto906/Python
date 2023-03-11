n=[]
color=[]
used=[]
ans=[]
for t in range(0,int(input())):
    p=int(input())
    e=int(input())
    n.clear()
    color.clear()
    used.clear()
    for i in range(0,p):
        n.append([])
        color.append(-1)
        used.append(-1)
    for i in range(0,p):
        for j in range(0,p):
            n[i].append(0)
    for i in range(0,e):
        s=list(map(int,input().split()))
        n[s[0]][s[1]]=1
        n[s[1]][s[0]]=1
    for i in range(0,p):
        for j in range(0,p):
            used[j]=-1
        for j in range(0,p):
            if n[i][j]==1 and color[j]!=-1:
                used[j]=1
        for j in range(0,p):
            if used[j]==-1:
                color[i]=j
                break
    ans=list(set(color))
    if len(ans)>2:
        print('F')
    else:
        print('T')