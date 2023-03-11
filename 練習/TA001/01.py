while True:
    try:
        s=int(input())
        s*=1000
        ans=(s-32000)*5/9000
        print('C=',int(ans),sep='')
    except:
        break