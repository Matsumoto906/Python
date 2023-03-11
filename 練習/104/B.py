g=int(input())
k=list(map(str,input().split(',')))
for t in range(g):
    s=list(map(str,input().split(',')))
    ans=[]
    for i in range(0,6):
        n=0
        a=s.copy()
        a.pop(i)
        for j in a:
            if j in k:
                n+=1
        ans.append(n)
    print(ans.count(2),ans.count(3),ans.count(4),ans.count(5),sep=',')