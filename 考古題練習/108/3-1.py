for t in range(int(input())):
    a,b=map(int,input().split())
    n=[]
    num=[]
    ans=''
    key=''
    for i in range(a):
       s=list(input())
       n.append(s)
    for k in range(b):
        num.clear()
        con=0
        for j in range(a):
            num.append(n[j][k])
        if num.count('T')>=con:
                con=num.count('T')
                key='T'
        if num.count('G')>=con:
                con=num.count('G')
                key='G'
        if num.count('C')>=con:
                con=num.count('C')
                key='C'
        if num.count('A')>=con:
                cpn=num.count('A')
                key='A'
        ans+=key
    print(ans)
