x=0
y=0
z=0
for i in range(int(input())):
    a,b,c,d=map(str,input().split())
    a=int(a)
    b=int(b)
    c=int(c)
    if a>x:
        x=a
        y=b
        z=c
        ans=d
    elif a==x:
        if b>y:
            x=a
            y=b
            z=c
            ans=d
        elif b==y:
            if c>z:
                x=a
                y=b
                z=c
                ans=d
print(ans)