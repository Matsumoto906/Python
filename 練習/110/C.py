a=0
b=0
for i in range(9):
    s=input()
    if s=='Tiger':
        a+=1
    else:
        b+=1
if a>b:
    print('Tiger')
else:
    print('Lion')