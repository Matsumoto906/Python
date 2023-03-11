s=list(map(int,input().split()))
ans=[]
for i in range(0,len(s)):
    a=s[i]
    for j in range(i+1,len(s)):
        if a>=s[j]:
            a-=s[j]
            break
    ans.append(a)
print(ans)