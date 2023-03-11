for t in range(1,int(input())+1):
    s=int(input())
    if s%400==0:
        print('Case ',t,': ','a leap year',sep='')
    elif s%100==0:
        print('Case ',t,': ','a normal year',sep='')
    elif s%4==0:
        print('Case ',t,': ','a leap year',sep='')
    else:
        print('Case ',t,': ','a normal year',sep='')