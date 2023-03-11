num=[2,3]
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
anum=[]
for i in num:
    if i<=s:
        anum.append(i)

ans=[]
for i in anum:
    if str(i)[::-1]==str(i):
        ans.append(i)

p=0
con=1
a=0
for i in ans:
    print('%-4d'%i,end='')
    if ans.index(i)+1==con:
        print()
        con=ans.index(i)+3+a
        a+=1
    p+=i
print()
print(p)


