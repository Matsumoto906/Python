while True:
    s=int(input())
    num=''
    if s==0:
        break
    for i in range(s):
        num+=(str(input()))+' '
    print(s)
    print(num[:-1])