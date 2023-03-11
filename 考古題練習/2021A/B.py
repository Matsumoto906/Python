while True:
    try:
        a,b=map(int,input().split())
        if a==0:
            if b==0:
                print('Tie')
            elif b==1:
                print('I lost')
            elif b==2:
                print('I won')
        elif a==1:
            if b==0:
                print('I won')
            elif b==1:
                print('Tie')
            elif b==2:
                print('I lost')
        elif a==2:
            if b==0:
                print('I lost')
            elif b==1:
                print('I won')
            elif b==2:
                print('Tie')
    except:
        break