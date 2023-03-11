def f(x):
    if x==4:
        return 'F'
    x=str(x)
    a=0
    for i in x:
        a+=int(i)**2
    if a==1:
        return 'T'
    else:
        return f(a)
for i in range(int(input())):
    s=int(input())
    print(f(s))