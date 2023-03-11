s=input()
key=int(input())
num=[]
ans=[]
for i in s:
    num.append(ord(i)-65)
for i in num:
    ans.append((i+key)%26)
for i in ans:
    print(chr(i+65),end='')