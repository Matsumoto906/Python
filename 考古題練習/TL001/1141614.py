s=input()
ans=0
k=0
for i in s:
    if i == '(':
        k+=1
        if k>ans:
            ans=k
    elif i == ')':
        k-=1
print(ans)