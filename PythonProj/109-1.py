num=[]
for i in range(0,4):
    num.append(eval(input()))

sum=0
for i in num:
    sum+=i

average=sum/4
all=''
for i in range(0,3):
    all+=str(num[i])+' '
all+=str(num[-1])
print(all)
print('Sum = %.2f'%sum)
print('Average = %.2f'%average)