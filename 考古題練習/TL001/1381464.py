s=list(map(int,input().split()))
s.sort()
print((s[-1]-1)*(s[-2]-1))