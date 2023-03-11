s=['1','2','3','4','5','6','7','8','9','0']
a,b=map(str,input().split())
key=True
for i in a:
    if i not in s:
        key=False
for i in b:
    if i not in s:
        key=False
if key==True:
    print(int(a)-int(b))
else:
    print('NaN')