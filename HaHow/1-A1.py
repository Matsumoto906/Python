a=int(input('請輸入初始值 :'))
b=int(input('請輸入結束值 :'))
ans=[]
for i in range(a,b+1):
    if i%7==0 or i%11==0:
        ans.append(i)
k=0
for i in ans:
    if k==10:
        print()
        k=0
    print('%-4d'%i,end='')
    k+=1
print()
print('總數共有',len(ans),'個')
print('數字總合為',sum(ans))