def f(x):
    if str(x)[::-1]==str(x):
        return x
    x+=int(str(x)[::-1])
    return f(x)

for t in range(int(input())):
    s=int(input())
    print(f(s))