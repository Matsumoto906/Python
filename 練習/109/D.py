for t in range(int(input())):
    s=int(input())
    a=0
    a+=s
    k=9
    num=[]
    ans=''
    while True:
        if k>=2:
            if s%k==0:
                s//=k
                num.append(k)
            else:
                k-=1
        else:
            break
    num.sort()
    g=1
    for i in num:
        ans+=str(i)
        g*=i
    if (g==a):
        print(ans)
    else:
       print(-1)