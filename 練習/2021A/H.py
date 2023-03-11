def f(x):
    for i in range(2,x):
        if i in num:
            break
        if x%i==0:
            num.append(i)
            num.append(x//i)
    return sum(num)

    

input()

s=list(map(int,input().split()))
for i in s:
    num=[1]
    x=f(i)
    if x==i:
        print('perfect')
    elif x>i:
        print('abundant')
    else:
        print('deficient')