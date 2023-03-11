

for t in range(int(input())):
    k=0
    a=0
    s=list(map(str,input().split()))
    for i in range(0,len(s)):
        b=s[i]
        if b != '+' and b != '-' and b != '==':
            b=float(b)*100
            b=round(b,0)
            s[i]=b
    for i in range(0,len(s)):
        if s[i]=='+':
            pass
        elif s[i]=='-':
            k-=float(s[i+1])*2
        elif s[i]=='==':
            a+=k
            k=0
        else:
            k+=float(s[i])
    if k==a:
        print('T')
    else:
        print('F')