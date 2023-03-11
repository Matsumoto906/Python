for t in range(int(input())):
    fib=[0,1]
    s=int(input())
    num=[]
    k=0+s
    ans=''

    while fib[-1]<s:
        fib.append(fib[-1]+fib[-2])
    if fib[-1]>s:
        fib.pop()
    
    fib=fib[::-1]
    fib.pop()
    fib.pop()

    for i in range(0,len(fib)):
        num.append(0)

    for i in range(0,len(fib)):
        if k==0:
            break
        if k in fib:
            num[fib.index(k)]=1
            k-=fib[fib.index(k)]
        else:
            
            k-=fib[i]
            num[i]=1

    if len(num)==0:
        print(s,'=1',sep='')
    else:
        for i in num:
            ans+=str(i)
        print(s,'=',ans,sep='')