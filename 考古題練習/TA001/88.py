s=input()
ans1=''
ans2=''
for i in s:
    if i not in ans1:
        ans1+=(i)
s=s[::-1]
for i in s:
    if i not in ans2:
        ans2+=i
ans2=ans2[::-1]
print(ans1)
print(ans2)