def f(x):
    num=[]
    for i in range(1,x):
        if x%i==0:
            num.append(i)
    return sum(num)

a,b=map(int,input().split())
if f(a)==b and f(b)==a:
    print('true')
else:
    print('false')