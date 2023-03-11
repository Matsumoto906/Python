s=int(input())
num=[1]
n=[]
for i in range(2,s):
    if i in n:
        break
    if s%i==0:
        num.append(i)
        num.append(s//i)
        n.append(s//i)
if sum(num)==s:
    print(True)
else:
    print(False)