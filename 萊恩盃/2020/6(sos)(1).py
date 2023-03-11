s=int(input())
n=input()
con=0
t=0
while True:
    if con==len(n):
        break
    for i in range(t,len(n),s):
        print(n[i],end='')
        con+=1
    t+=1