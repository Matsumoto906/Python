s=input()
k=[]
ans=[]
a=s[::-1]
for i in s:
    if i not in k:
        k.append(i)
for i in k:
    print(i,end='')

print()

for i in a:
    if i not in ans:
        ans.append(i)
ans=ans[::-1]
for i in ans:
    print(i,end='')