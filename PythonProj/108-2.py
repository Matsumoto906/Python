s=int(input())
ans=0
p=-1
if s>1:
    for i in range(3,2*s,2):
        ans+=p*(1/i)
        p*=-1
    ans+=1
else:
    ans=1
ans*=4
print('%.4f'%ans)