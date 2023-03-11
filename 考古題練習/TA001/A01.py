while True:
    try:
        s=int(input())
        s*=1000
        ans=(s-32000)*5000//9000
        ans/=1000
        print('C=%d'%ans)
    except:
        break