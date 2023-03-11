s=input().split()
num=s.copy()
num.sort()
ans=0
for i in range(0,len(s)):
    if s[i] != num[i]:
        ans+=1
print(ans)