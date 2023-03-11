s=input().split()
n=''
num=[[],[],[]]
d=[]
a=''
o=0
x=0

for i in range(1,10):
    n+=(s[i-1])
    if i%3==0:
        n+=(',')

n=n.strip(n[-1])
k=n.split(',')

for i in range(0,3):
    num[i]=k[i]
for i in num:
    d.append('-')
    for j in i:
        d.append(j)
for i in range(1,len(d)):
    a+=d[i]

if  num[0][0]=='O' and num[0][1]=='O' and num[0][2]=='O':
    o+=1
if  num[1][0]=='O' and num[1][1]=='O' and num[1][2]=='O':
    o+=1
if  num[2][0]=='O' and num[2][1]=='O' and num[2][2]=='O':
    o+=1
if  num[0][0]=='O' and num[1][0]=='O' and num[2][0]=='O':
    o+=1
if  num[0][1]=='O' and num[1][1]=='O' and num[2][1]=='O':
    o+=1
if  num[0][2]=='O' and num[1][2]=='O' and num[2][2]=='O':
    o+=1
if  num[0][0]=='O' and num[1][1]=='O' and num[2][2]=='O':
    o+=1
if  num[2][0]=='O' and num[1][1]=='O' and num[0][2]=='O':
    o+=1
if  num[0][0]=='X' and num[0][1]=='X' and num[0][2]=='X':
    x+=1
if  num[1][0]=='X' and num[1][1]=='X' and num[1][2]=='X':
    x+=1
if  num[2][0]=='X' and num[2][1]=='X' and num[2][2]=='X':
    x+=1
if  num[0][0]=='X' and num[1][0]=='X' and num[2][0]=='X':
    x+=1
if  num[0][1]=='X' and num[1][1]=='X' and num[2][1]=='X':
    x+=1
if  num[0][2]=='X' and num[1][2]=='X' and num[2][2]=='X':
    x+=1
if  num[0][0]=='X' and num[1][1]=='X' and num[2][2]=='X':
    x+=1
if  num[2][0]=='X' and num[1][1]=='X' and num[0][2]=='X':
    x+=1

if x>o:
    print('X')
elif x<o:
    print('O')
else:
    print('平手')