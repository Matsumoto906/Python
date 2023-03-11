for t in range(int(input())):
    a,b=input().split(',')
    if a=='Y':
        if b=='P':
            print(1)
        elif b=='O':
            print(2)
        else:
            print(0)
    elif a=='O':
        if b=='P':
            print(2)
        elif b=='O':
            print(0)
        else:
            print(1)
    elif a=='P':
        if b=='P':
            print(0)
        elif b=='O':
            print(1)
        else:
            print(2)