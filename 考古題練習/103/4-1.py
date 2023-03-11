password={
    '00':'0','01':'1','100':'2','101':'3',
    '1100':'4','1101':'5','11100':'6',
    '11101':'7','111100':'8','111101':'9'
}
for t in range(int(input())):
    s=input()
    n=[[],[]]
    k=''
    if s[0:2] in password:
        n[0]=password[s[0:2]]
        s=s[2:]
    else:
        n[0]=password[s[0:3]]
        s=s[3:]
    n[1]=password[s]
    for i in n:
        k+=i
    if k=='24':
        print('A')
    elif k=='25':
        print('B')
    elif k=='26':
        print('C')
    else:
        print(chr(int(k)+67))