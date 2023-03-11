s=list(map(int,input().split(', ')))
for i in range(2):
    for j in range(0,len(s)-1):
        if s[j] >s[j+1]:
            a=s[j]
            b=s[j+1]
            s[j]=b
            s[j+1]=a
print(s)