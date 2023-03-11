def f(x):
    x=str(x)
    n=0
    for i in x:
        n+=int(i)*int(i)
    if n==4:
        return False
    elif n==1:
        return True
    else:
        return f(n)
s=input()
print(f(s))