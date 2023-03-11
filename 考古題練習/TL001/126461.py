ans=0
a=int(input())
b=int(input())
a=str(bin(a))[2:].zfill(100)
b=str(bin(b))[2:].zfill(100)
for i in range(0,len(a)) :
    if a[i]!=b[i]:
        ans+=1
print(ans)