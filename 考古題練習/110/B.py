s=int(input())
if s%400==0:
    print('a leap year')
elif s%100==0:
    print('a normal year')
elif s%4==0:
    print('a leap year')
else:
    print('a normal year')