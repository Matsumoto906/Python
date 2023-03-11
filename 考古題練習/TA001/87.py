a,b=map(int,input().split())
a=str(bin(a))
b=str(bin(b))
a=a[2:]
b=b[2:]
a=a.zfill(20)
b=b.zfill(20)
ans=0
for i in range(0,20):
    if a[i] != b[i]:
        ans+=1
print(a)
print(b)
print(ans)