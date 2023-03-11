for j in range(0,int(input())):
    s=str(input())
    a=''
    b=''
    for i in s:
        if i=='4':
            a+='3'
        else:
            a+=i
    b=int(s)-int(a)
    print(a,b)