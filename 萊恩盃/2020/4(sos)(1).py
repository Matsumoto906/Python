input()
name=list(map(str,input().split()))
num=list(map(float,input().split()))
ans=0
for i in range(len(num)):
    k=num.index(max(num))
    a=name.pop(k)
    b=num.pop(k)
    c=str(bin(ans))[2:]
    ans+=1
    print(a,':',c)