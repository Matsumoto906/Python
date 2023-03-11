while True:
    try:
        s=float(input())
        s*=1000
        s*=0.000454
        s=round(s,2)
        print(s)
    except:
        break