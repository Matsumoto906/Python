a,b,c=map(int,input().split())
lcm=0
for i in range(1,min(a,b,c)+1):
    if a%i==0 and b%i==0 and c%i==0:
        gcd=i
for i in range(max(a,b,c),a*b*c+1,min(a,b,c)):
    if i%a==0 and i%b==0 and i%c==0:
        lcm=i
        break
if lcm==0:
    lcm=a*b*c
print('GCD=',gcd,sep='')
print('LCM=',lcm,sep='')