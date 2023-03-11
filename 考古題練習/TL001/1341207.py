s=input().split()
num=[]
a=list(set(s))
for i in a:
    num.append(s.count(i))
n=list(set(num))
if len(n)== len(num):
    print(True)
else:
    print(False)