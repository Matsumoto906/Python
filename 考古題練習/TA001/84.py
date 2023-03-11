num=[2,3]
g=[]
ans=[]
k=[2,3,5]
a=False
def f(x):
    key=True
    for i in range(0,len(num)):
        if x%num[i]==0:
            key=False
            break
    return key

s=int(input())
for i in range(4,s+1):
    if f(i)==True:
        num.append(i)
for i in range(1,s+1):
    if s%i==0:
        g.append(i)
for i in g: 
    if i in num:
        ans.append(i)
for i in ans:
    if i not in k:
        a=True
        break
if a==True:
    print('False')
else:
    print('True')