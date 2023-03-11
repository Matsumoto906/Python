for i in range(int(input())):
    s=input().split()
    con=0
    print(len(s),end=',')
    for i in s:
        if 's' in i or 'S' in i:
            con+=1
    print(con)