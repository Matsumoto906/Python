for t in range(int(input())):
    num=''
    for i in range(3):
        s=input()
        num+=s
    if num[0]==num[1]==num[2] or num[0]==num[3]==num[6] or num[0]==num[4]==num[8]:
        if num[0]=='0':
            print(3)
        else:
            print(num[0])
    elif num[1]==num[4]==num[7] or num[3]==num[4]==num[5] or num[2]==num[4]==num[6]:
        if num[4]=='0':
            print(3)
        else:
            print(num[4])
    elif num[2]==num[5]==num[8] or num[6]==num[7]==num[8]:
        if num[8]=='0':
            print(3)
        else:
            print(num[8])
    else:
        print(3)