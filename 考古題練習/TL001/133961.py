s=list(map(int,input().split()))
n=len(s)
n//=2
for i in s:
    if s.count(i) == n:
        print(i)
        break