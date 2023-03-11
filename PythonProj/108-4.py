num=[]
while True:
    s=int(input())
    if s==-9999:
        break
    num.append(s)
n=0
ans=0
for i in num:
    ans+=i
    if ans<0:
        ans=0
    if ans>n:
        n=ans
print((n))