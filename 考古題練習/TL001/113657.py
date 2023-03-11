s=input()
a=0
b=0
for i in s:
    if i == 'U':
        a+=1
    elif i == 'D':
        a-=1
    elif i == 'L':
        b+=1
    elif i == 'R':
        b-=1
if a==0 and b==0:
    print(True)
else:
    print(False)