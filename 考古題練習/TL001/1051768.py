a=input()
b=input()
ans=''
l=min(len(a),len(b))
for i in range(0,l):
    ans+=a[i]+b[i]
if l==len(a):
    ans+=b[l:]
else:
    ans+=a[l:]
print(ans)