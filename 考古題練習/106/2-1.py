for t in range(int(input())):
    s=input()
    num1=[]
    num2=0
    for i in range(0,len(s)):
        if i % 2 == 0:
            num1.append(str(int(s[i])*2))
        else:
            num1.append((s[i]))
    
    for i in num1:
        for j in range(0,len(i)):
            num2+=int(i[j])

    if num2%10==0:
        print('T')
    else:
        print('F')
        
    