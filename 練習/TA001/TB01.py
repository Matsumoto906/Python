s=list(map(int,input().split(', ')))
a=s.copy()
x=a.pop(a.index(max(a)))
y=a.pop(a.index(max(a)))
for i in range(len(s)):
    for j in range(0,len(s)-1):
        if s[-1]==x and s[-2]==y:
            break
        if s[j]>s[j+1]:
            a=s[j]
            b=s[j+1]
            s[j]=b
            s[j+1]=a
            
print(s)