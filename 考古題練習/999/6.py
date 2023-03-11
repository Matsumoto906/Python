while True:
    try:
        s=input().split()
        n=s.pop()
        num=''
        for i in s:
            num+=i
        num=list(map(int,num.split(',')))
        key=False
        for i in range(0,len(num)):
            for j in range(0,len(num)):
                if num[i] + num[j] == int(n) and i != j:
                    print(i,j)
                    key=True
                    break
            if key == True:
                break
        if key == False:
            print('F')
    except:
        break