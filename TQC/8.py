s=input()
ans=0
for i in s:
    print('ASCII code for \'',i,'\' is ',ord(i),sep='')
    ans+=ord(i)
print(ans)