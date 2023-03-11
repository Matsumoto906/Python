for i in range(int(input())):
    s=list(map(int,input().split()))
    s.sort()
    print(s[-1],s[-2])