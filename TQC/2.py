s=int(input())
if s%5==0 and s%3==0:
    print(s,'is a multiple of 3 and 5.')
elif s%3==0:
    print(s,'is a multiple of 3.')
elif s%5==0:
    print(s,'is a multiple of 5.')
else:
    print(s,'is not a multiple of 3 or 5.')