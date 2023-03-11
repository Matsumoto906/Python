s=list(map(int,input().split()))
s=sorted(s,reverse=True)
ans=0
for i in range(1,len(s),2):
    ans+=min(s[i],s[i-1])
print(ans)