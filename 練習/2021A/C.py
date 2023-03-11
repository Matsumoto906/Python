while True:
    s=int(input())
    if s==0:
        break
    num=[]
    for i in range(s):
        a=input()
        num.append(a)
    for i in range(0,len(num)-1):
        print(num[i]+' ',end='')
    print(num[-1])