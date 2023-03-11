x=0
y=0
z=0
n=''
for t in range(int(input())):
    s=list(map(str,input().split()))
    a=s[0]
    b=s[1]
    c=s[2]
    d=s[3:]
    if int(a)>x:
        x=int(a)
        y=int(b)
        z=int(c)
        ans=d
    elif int(a)==x:
        if int(b)>y:
            x=int(a)
            y=int(b)
            z=int(c)
            ans=d
        elif int(b)==y:
            if int(c)>z:
                x=int(a)
                y=int(b)
                z=int(c)
                ans=d

for i in ans:
    n+=i+' '
n=n.strip()
print(n)