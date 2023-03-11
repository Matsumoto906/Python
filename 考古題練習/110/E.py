while True:
    try:
        s=(input())
        num=[]
        for i in s:
            num.append(int(i))
        print(sum(num))
    except:
        break