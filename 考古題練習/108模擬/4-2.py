s=1
g=1
for i in range(1,2147483648):
    s*=i
for i in range(1,2147483647):
    g*=i

print(s//(1*g))
