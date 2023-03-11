def f(x):
    key=True
    for i in range(0,len(num)):
        if x%num[i]==0:
            key=False
            break
    return key

while True:
    num=[2,3]
    s=int(input('請輸入整數 :'))
    if s==-9999:
        break
    for i in range(4,s+1):
        if f(i)==True:
            num.append(i)
    if s in num:
        print(s,'為質數',sep='')
    else:
        print(s,'為非質數',sep='')