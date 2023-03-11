def f(a,b,c,d):
    if c==0 or d==0:
        return 0
    elif a[c-1]==b[d-1]:
        return f(a,b,c-1,d-1)+1
    else:
        return max(f(a,b,c-1,d),f(a,b,c,d-1))

x=input()
y=input()
print(f(x,y,len(x),len(y)))