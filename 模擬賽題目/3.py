import itertools
num=[]
while True:
    try:
        s=list(map(float,input().split(',')))
        num.append(s)
    except:
        break
num=list(itertools.permutations(num,2))
n=[]

for i in num:
    k=((i[1][0]-i[0][0])**2+(i[1][1]-i[0][1])**2)**0.5
    n.append(k)
ans=n.index(min(n))

a=num[ans][0][0]
b=num[ans][0][1]
c=num[ans][1][0]
d=num[ans][1][1]
e=n[ans]
print(num[ans])
print('(','%.2f'%a,',','%.2f'%b,'),(','%.2f'%c,',','%.2f'%d,'),','%.4f'%e ,sep='')