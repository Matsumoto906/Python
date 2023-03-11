for t in range(int(input())):
    a,b,c,d=map(int,input().split())
    if c>a:
        if d<b:
            c-=1
            d+=60
        ans=d-b+(c-a)*60
    elif c<a:
        if b<d:
            a-=1
            b+=60
        ans=1440-(60*(a-c)+b-d)
    else:
        if d-b>=0:
            ans=d-b
        else:
            ans=1440-(b-d)
        
    print(ans)