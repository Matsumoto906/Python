for t in range(int(input())):
    s=list((input().split()))
    num=[]
    for i in s:
        if i == '+':
            k=(num[-2])+(num[-1])
            num.remove(num[-1])
            num.remove(num[-1])
            num.append(k)
        elif i == '-':
            k=(num[-2])-(num[-1])
            num.remove(num[-1])
            num.remove(num[-1])
            num.append(k)
        elif i == '*':
            k=(num[-2])*(num[-1])
            num.remove(num[-1])
            num.remove(num[-1])
            num.append(k)
        elif i == '/':
            k=(num[-2])//(num[-1])
            num.remove(num[-1])
            num.remove(num[-1])
            num.append(k)
        else:
            num.append(int(i))
    print(num[-1])