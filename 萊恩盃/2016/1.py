s=input()
num=[]
for i in s:
    num.append(ord(i))

print('%.3f'%(sum(num)/len(s)))