def f(x):
    x=str(x)
    for i in range(0,len(x)):
        if int(x[0:i+1])%(i+1)==0:
            key=True
        else:
            key=False
            break
        if key==True:
            if len(x)!=len(set(x)):
                key=False
    return key

s=int(input())
for i in range(9*int(str(1)*s),0,-1):
    if f(i)==True:
        print(i)
        break
