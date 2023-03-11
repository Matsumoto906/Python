s=list(map(str,input().split()))
ans=0
for i in s:
    if s.count(i)==1:
        ans+=int(i)
print(ans)