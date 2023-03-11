def f(a):
    key=False
    if str(a)==str(a)[::-1]:
        key=True
    if key==True:
        return (a)
    else:
        return f(int(str(a)[::-1])+int(a))
        

for i in range(0,int(input())):
    s=input()
    print(f(s))