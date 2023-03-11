while True:
    s=int(input())
    if s>0 and s<=10000:
        for i in range(1,s):
            if i%7!=0:
                print(i,end=' ')
    print()
    if s==0:
        break