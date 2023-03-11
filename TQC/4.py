num=[]
ans=9999
while True:
    s=int(input())
    if s==9999:
        break
    if s<ans:
        ans=s
print(ans)