s=input()
ans=''
for i in range(0,len(s)):
    if s[i]=='[':
        a=i+1
        x=int(s[i-1])
    elif s[i]==']':
        b=i
t=s[a:b]*x

key=True
for i in range(0,len(s)):
    if i>=a-2 and i<=b:
        if key==False:
            continue
        else:    
            ans+=t
            key=False
    else: 
        ans+=s[i]
print(ans)
