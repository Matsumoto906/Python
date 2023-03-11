n=['1','2','3','4','5','6','7','8','9','0']
a,b=map(str,input().split())
k=True
for i in a:
    if i not in n:
        k=False
        break
for i in b:
    if i not in n:
        k=False
        break
if k==True:
    print((int(a)-int(b)))
else:
    print('NaN')