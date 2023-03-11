for t in range(int(input())):
    a,b=map(str,input().split('/'))
    a=(a).split('.')
    b=(b).split('.')
    n=[]
    b1=[]
    b2=[]
    l=''
    ans=''
    for i in b:
        n.append(str(abs(int(i)-255)))
    for i in a:
        k=bin(int(i))[2:]
        k=k.zfill(8)
        b1.append(k)
    for i in n:
        k=bin(int(i))[2:]
        k=k.zfill(8)
        b2.append(k)
    for i in range(0,4):
        for j in range(0,8):
            if b1[i][j]=='1' or b2[i][j]=='1':
                l+=('1')
            else:
                l+='0'
        l+=('.')
    l=l.strip('.')
    l=l.split('.')
    for i in l:
        ans+=str(int(i,2))+'.'
    ans=ans.strip('.')
    print(ans)