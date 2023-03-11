for t in range(int(input())):
    a,b=map(int,input().split())
    tot_num=[]
    k_num=[]
    ans=0
    start=list(map(int,input().split()))
    n=start.copy()
    k=int(input())
    for i in range(k):
        s=list(map(int,input().split()))
        k_num.append(s)
    k_num.sort()
    for i in k_num:
        x=abs(i[0]-n[0])
        y=abs(i[1]-n[1])
        ans+=x+y
        n=i
    ans+=abs(n[0]-start[0])
    ans+=abs(n[1]-start[1])
    print('The shortest path has length',ans)