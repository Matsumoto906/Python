while True:
    try:
        a,b=map(int,input().split())
        print(a//b,a%b)
    except:
        break