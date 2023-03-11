x=0
o=0
num=list(map(str,input().split()))

if  num[0]=='O' and num[1]=='O' and num[2]=='O':
    o+=1
if  num[3]=='O' and num[4]=='O' and num[5]=='O':
    o+=1
if  num[6]=='O' and num[7]=='O' and num[8]=='O':
    o+=1
if  num[0]=='O' and num[3]=='O' and num[6]=='O':
    o+=1
if  num[1]=='O' and num[4]=='O' and num[7]=='O':
    o+=1
if  num[2]=='O' and num[5]=='O' and num[8]=='O':
    o+=1
if  num[0]=='O' and num[4]=='O' and num[8]=='O':
    o+=1
if  num[2]=='O' and num[4]=='O' and num[6]=='O':
    o+=1
if  num[0]=='X' and num[1]=='X' and num[2]=='X':
    x+=1
if  num[3]=='X' and num[4]=='X' and num[5]=='X':
    x+=1
if  num[6]=='X' and num[7]=='X' and num[8]=='X':
    x+=1
if  num[0]=='X' and num[3]=='X' and num[6]=='X':
    x+=1
if  num[1]=='X' and num[4]=='X' and num[7]=='X':
    x+=1
if  num[2]=='X' and num[5]=='X' and num[8]=='X':
    x+=1
if  num[0]=='X' and num[4]=='X' and num[8]=='X':
    x+=1
if  num[2]=='X' and num[4]=='X' and num[6]=='X':
    x+=1

if o>x:
    print('O')
elif x==o:
    print('平手')
else:
    print('X')