while True:
    try:
        a,b,c=map(int,input().split())
        k=(a+b+c)/2
        s1=int(abs(k-b-c))
        s2=int(abs(k-a-c))
        s3=int(abs(k-a-b))
        print(s2,s3,s1)
    except:
        break