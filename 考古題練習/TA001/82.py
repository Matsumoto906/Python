s=int(input())
num=[]
ans=0
for i in range(1,s):
    if s%i==0:
        num.append(i)
for i in num:
    ans+=i
if ans == s :
    print('True')
else:
    print('False')