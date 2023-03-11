a=list(input())
b=list(input())
a.sort()
b.sort()
k=True
for i in range(0,len(a)):
    if a[i] != b[i]:
        k=False
        break
print(k)