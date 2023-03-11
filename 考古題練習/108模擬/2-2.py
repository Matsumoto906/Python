for i in range(int(input())):
    s=input()
    ans=0

    for i in s:
        ans+=int(i)**len(s)
    if str(ans)==s:
        print('Y')
    else:
        print('N')