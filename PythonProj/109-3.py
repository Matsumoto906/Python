s=int(input())
ans=0
for i in range(2,s+1):
    ans+=1/((i-1)**0.5+(i)**0.5)
print('%.4f'%ans)