for t in range(int(input())):
    num=[]
    ans=0
    l=int(input())
    n=list(map(int,input().split()))
    n.sort()
    n=n[::-1]
    while True:
        if l<3:
            break
        l-=3
        num.append(n[2])
        n.remove(n[0])
        n.remove(n[0])
        n.remove(n[0])
    for i in num:
        ans+=i
    print(ans)