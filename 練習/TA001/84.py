num=[2,3]
def f(x):
    key=True
    for i in num:
        if x%i==0:
            key=False
            break
    return key
for i in range(4,10001):
    if f(i)==True:
        num.append(i)
s=int(input())
n=[1]
ans=[]
for i in range(2,s):
    if i in n:
        break
    if s%i==0:
        n.append(i)
        n.append(s//i)
for i in n:
    if i in num:
        ans.append(i)

for i in ans:
    if i==2 or i==3 or i==5:
        key=True
    else:
        key=False
        break

print(key)