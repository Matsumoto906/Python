s=input('請輸入一個字串 :')
ans=0
for i in s:
    print('ASCll code for','\'',i,'\'','is ',ord(i),sep='')
    ans+=ord(i)
print(ans)