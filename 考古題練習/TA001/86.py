s=int(input())
while True:
    if s==1:
        print(True)
        break
    elif s==4:
        print(False)
        break
    else:
        num=0
        for i in str(s):
            num+=int(i)**2
        s=num
