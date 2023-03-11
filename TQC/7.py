a=list()
b=list()
while True:
    s=int(input())
    if s==-9999:
        break
    a.append(s)
while True:
    s=int(input())
    if s==-9999:
        break
    a.append(s)
b=tuple(a)
a.sort()
print('Combined tuple before sorting:',b)
print('Combined list after sorting:',a)