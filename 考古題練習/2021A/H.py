
input()
s=list(map(int,input().split()))
for i in s:
    num=0
    for j in range(1,i):
        if i%j==0:
            num+=(j)
    if(num) == i:
        print('perfect')
    elif (num)>i:
        print('abundant')
    else:
        print('deficient')