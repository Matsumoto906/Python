input()
k=0
num=list(map(int,input().split()))
for i in range(0,len(num)):
    if min(num[i],num[i+1]) > k:
        