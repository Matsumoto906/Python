a=0
b=0
for i in range(9):
    s=input()
    if s=='Tiger':
        a+=1
    elif s=='Lion':
        b+=1
if a>b:
    print('Tiger')
elif b>a:
    print('Lion')