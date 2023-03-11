from datetime import timedelta
from datetime import datetime
for t in range(int(input())):
    s=int(input())
    n=timedelta(days=1)
    now=datetime(1970,1,1)
    ans=now+n*s
    b=(str(ans.month).zfill(2))
    c=(str(ans.day).zfill(2))
    print(ans.year,b,c,sep='-')