s=input().split()
ans=''
for j in s[0]:
    k=True
    for i in range(0,len(s)):
        if j not in s[i]:
            k=False
            break
        else:
            s[i]=s[i].replace(j,'',1)
    if k==True:
        ans+=j
print(ans)